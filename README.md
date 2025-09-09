# Expense Tracker (MERN)

Minimal full-stack app with authentication and CRUD transactions.

## Backend setup
```
cd backend
cp .env.example .env
# edit .env if needed
npm install
npm run dev
```
API will run on http://localhost:5000

## Frontend setup
```
cd frontend
npm install
# set backend url if different:
# echo "VITE_API_URL=http://localhost:5000/api" > .env
npm run dev
```

## Notes
- Signup to create a user, then login.
- Add income/expense on Dashboard; summary auto-updates.
