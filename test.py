from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoginData(BaseModel):
    email: str
    password: str

class PredictResult(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "hello fastapi initiated"}

@app.get("/about")
def about():
    return {"message":"hello about section"}

@app.get("/about/{name}")
def profile(name: str): 
    return { "message": f"hello {name} welcome"}    

@app.get("/test")
def welcome(name:str, age:int):
    return {"name": {name}, "age": {age}}

@app.post("/login")
def auth():
    return {"message": "login request succesfully receieved"}
    
@app.post("/login-data")
def logindata(data: LoginData):
    return {"message": f"login succesful for {data.email}"}

@app.post("/predict")
def prediction(data: PredictResult):
    text = data.text.lower()

    if "happy" in text or "good" in text or "great" in text:
        result = "positive"
    elif "sad" in text or "worry" in text or "cry" in text:
        result = "negative"
    else:
        result = "neutral"    


    return {
        "input": data.text,
        "prediction": result
    }    