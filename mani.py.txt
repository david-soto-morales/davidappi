from fastapi import FastaAPI

app=FastAPI()

@app.get("/")
def index():
    return "hola a todo "
