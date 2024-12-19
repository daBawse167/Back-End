from fastapi import FastAPI, HTTPException
from schemas import signup
from config import add_user

#create app
app = FastAPI()

#endpoint for registering
@app.post("/register")
def register_user():
    details = signup()
    add_user(details)
    return {"message": "user registered"}

#base
@app.get("/")
async def root():
    return {"message": "home"}