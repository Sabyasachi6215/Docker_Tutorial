from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"Hello": "World" "I am creating docker Images for fastapi Application"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
