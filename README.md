# Loan Engine

Laenuotsuste mootor, mis hindab laenetaotluse ja tagastab maksimaalse heakskiidetava summa ning perioodi. Süsteem kasutab isikukoodi põhist krediidimoodifitseerijat, et määrata, kui suurt laenu klient saada võib.

## Tehniline ülevaade

- **Backend:** Python / FastAPI
- **Frontend:** React / TypeScript / Vite (Peamiselt genereeritud AI abil, sest TypeScript pole väga tugev külg)

#### Eeldused:
- Python 3.10+
- Node.js 18+

## Käivitamine

### Backend

```bash
cd backend
pip install fastapi uvicorn
uvicorn main:app --reload
```

Backend käib aadressil `http://localhost:8000`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend käib aadressil `http://localhost:5173`.

Ava brauser aadressil **http://localhost:5173**.

## Testisikukoodid

| Isikukood     | Olek         |
|---------------|--------------|
| 49002010965   | Võlglane     |
| 49002010976   | Segment 1    |
| 49002010987   | Segment 2    |
| 49002010998   | Segment 3    |

## API

### `POST /loan-decision`

**Päring:**
```json
{
  "personal_code": "49002010987",
  "loan_amount": 5000,
  "loan_period": 24
}
```

**Vastus:**
```json
{
  "approved": true,
  "approved_amount": 7200,
  "approved_period": 24,
  "message": "Requested 5000€. Approved up to 7200€."
}
```