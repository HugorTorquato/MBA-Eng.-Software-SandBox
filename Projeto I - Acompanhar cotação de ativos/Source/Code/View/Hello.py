from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"message":"Hello, FastAPI"}

# Command to run in the venv attach_shell terminal ( To make it available actually )