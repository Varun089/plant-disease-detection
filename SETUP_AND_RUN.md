# Plant Disease Detection - Quick Setup & Run Guide

## ⚡ FASTEST WAY TO RUN (Docker)

### Prerequisites:
- Docker installed
- Docker Compose installed

### Run in 2 Commands:
```bash
git clone https://github.com/Varun089/plant-disease-detection.git
cd plant-disease-detection
docker-compose up --build
```

**Then open:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000/api/health
- Database: PostgreSQL on localhost:5432

---

## 🚀 Manual Setup (Local)

### Backend Setup:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Backend runs on: http://localhost:5000

### Frontend Setup (New Terminal):
```bash
cd frontend
npm install
npm start
```
Frontend runs on: http://localhost:3000

---

## 📋 API Endpoints Available:

- `GET /api/health` - Health check
- `GET /api/info` - API information
- `POST /api/predict` - Image prediction
- `POST /api/sensor-data` - Submit sensor data
- `GET /api/recommendations` - Get recommendations

---

## ✅ Verify Installation:

```bash
curl http://localhost:5000/api/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "Plant Disease Detection API",
  "version": "1.0.0"
}
```

---

## 🔧 Troubleshooting:

**Port already in use?**
```bash
# Kill process on port 5000
kill -9 $(lsof -t -i:5000)  # Mac/Linux
# Windows: netstat -ano | findstr :5000 then taskkill /PID <PID> /F
```

**Module not found?**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📊 Project Structure:
- `/backend` - Flask API + ML models
- `/frontend` - React dashboard
- `docker-compose.yml` - Container orchestration
- `requirements.txt` - Python dependencies

---

**Ready to run! Choose Docker (fastest) or manual setup above.**
