from fastapi import *
from typing import Optional
from models import UserAccess

app = FastAPI(
    docs_url="/"
)


@app.post("/api/users/signup", tags=["Usuario"])
def SignUp(user: UserAccess): 
    return {"Hello": "World"}

