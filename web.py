from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def view():
    return {"message": "Flaxem Systems"}