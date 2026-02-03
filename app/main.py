from fastapi import FastAPI
from app.services.weather_service import fetch_weather

app = FastAPI()

@app.get("/weather")
def weather(city: str):
    result = fetch_weather(city)
    if not result:
        return{"error":"city not found"}
    return result


@app.get("/")
def root():
    return {"message": "Backend is running!"}

@app.get("/hello")
def hello(name:str):
    return {"message": f"Hello {name}"}

@app.get("/ashok")
def ashok():
    return({"Hi ! IM Ashokkumar Backend Developer"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
    