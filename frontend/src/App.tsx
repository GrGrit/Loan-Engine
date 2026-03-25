import { useState } from 'react'
import './App.css'

interface LoanDecision {
  approved: boolean
  approved_amount: number | null
  approved_period: number | null
  message: string
}

function App() {
  const [personalCode, setPersonalCode] = useState('')
  const [loanAmount, setLoanAmount] = useState(2000)
  const [loanPeriod, setLoanPeriod] = useState(12)
  const [result, setResult] = useState<LoanDecision | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch('http://localhost:8000/loan-decision', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          personal_code: personalCode,
          loan_amount: loanAmount,
          loan_period: loanPeriod,
        }),
      })

      if (!response.ok) {
        const data = await response.json()
        throw new Error(data.detail ?? 'Viga päringu töötlemisel')
      }

      const data: LoanDecision = await response.json()
      setResult(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Tundmatu viga')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <h1>Laenuotsus</h1>

      <form className="loan-form" onSubmit={handleSubmit}>
        <div className="field">
          <label htmlFor="personal-code">Isikukood</label>
          <input
            id="personal-code"
            type="text"
            value={personalCode}
            onChange={e => setPersonalCode(e.target.value)}
            required
          />
        </div>

        <div className="field">
          <label htmlFor="loan-amount">Laenusumma (€)</label>
          <input
            id="loan-amount"
            type="number"
            min={2000}
            max={10000}
            value={loanAmount}
            onChange={e => setLoanAmount(Number(e.target.value))}
            required
          />
          <span className="hint">2 000 – 10 000 €</span>
        </div>

        <div className="field">
          <label htmlFor="loan-period">Periood (kuud)</label>
          <input
            id="loan-period"
            type="number"
            min={12}
            max={60}
            value={loanPeriod}
            onChange={e => setLoanPeriod(Number(e.target.value))}
            required
          />
          <span className="hint">12 – 60 kuud</span>
        </div>

        <button type="submit" disabled={loading}>
          {loading ? 'Arvutan...' : 'Taotle laenu'}
        </button>
      </form>

      {error && <div className="result error">{error}</div>}

      {result && (
        <div className={`result ${result.approved ? 'approved' : 'rejected'}`}>
          <p className="status">{result.approved ? 'Heaks kiidetud' : 'Tagasi lükatud'}</p>
          {result.approved_amount != null && (
            <p>Summa: <strong>{result.approved_amount.toLocaleString('et-EE')} €</strong></p>
          )}
          {result.approved_period != null && (
            <p>Periood: <strong>{result.approved_period} kuud</strong></p>
          )}
          <p>{result.message}</p>
        </div>
      )}
    </div>
  )
}

export default App
