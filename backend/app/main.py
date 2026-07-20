from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to Retail Intelligence Platform"
    }

@app.get("/about")
def about():
    return {
        "project": "Retail Intelligence Platform",
        "developer": "Harshitha",
        "backend": "FastAPI"
    }