from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message":"Hello World"}

@app.get("/PIAIC")
def piaci():
    return {"organization":"PIAIC"}