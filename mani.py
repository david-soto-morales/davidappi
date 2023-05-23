from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return "hola a todos "
@app.get("/tortas/{num}")
def dav(num):
    return num
