from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import engine
from core.models.appointment import Appointment
from routes import appointments

# Create tables
Appointment.__table__.create(bind=engine, checkfirst=True)

# Create FastAPI app
app = FastAPI()

# ✅ Enable CORS for frontend at http://localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Only allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


# Register appointment routes
app.include_router(appointments.router)
