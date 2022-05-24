from fastapi import FastAPI, Path
from pydantic import BaseModel
import secrets
import string

app = FastAPI()

@app.get("/")
def index():
    return{"Name": "Index Page"}

@app.post("/generate-password/")
def generate_password(char_amount: int):
    #generate a string contaning all characters we want to use
    password_set = string.ascii_letters + string.digits + string.punctuation
    if(char_amount<=18 and char_amount >=8 ):
        password = ''.join(secrets.choice(password_set) for i in range(char_amount))
        return password
    else:
        return {"Error": "Password must be between 8 or 18 "}
    
    