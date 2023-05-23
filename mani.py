from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return "hola a todos "
@app.get("/tortas")
def dav():
    return" este mensaje esta chido"
