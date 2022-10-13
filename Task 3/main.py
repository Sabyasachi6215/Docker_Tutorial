from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"Hello": "World" "I am creating docker Images for fastapi Application"}