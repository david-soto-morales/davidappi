from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return "hola a todos "
@app.get("/tortas/{num}")
def dav(num):
    return num
@app.get("/conversor_caf/{C}")
def temp{C}:
     try:
            C=float(C)
            TF=C*(9/5) + 32
            return f"la temperatura es de {TF} grados sentigrados"
    except:
            return"eso no era"
