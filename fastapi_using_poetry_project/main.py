from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"Hello":"World"}

@app.get("/PIAIC")
def piaci():
    return {"organization":"PIAIC"}