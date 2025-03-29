from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root ():
    return {"message": "atualização de código"}
@app.get("/teste1")
async def root ():
    return {"message": "É nois queros"}