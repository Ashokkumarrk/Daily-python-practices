from fastapi import FastAPI
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/")
def read_root():
    return {"Notes app is running"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)