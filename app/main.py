from fastapi import FastAPI
from app.routers import compliance

app = FastAPI()

# Mount the compliance verified image analyzer router
app.include_router(compliance.router)

@app.get("/")
def root():
    return {"status": "VeriHome System Online"}
