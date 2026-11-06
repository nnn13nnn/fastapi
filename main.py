from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Το API δουλεύει στο Cloud (Render)!"}
