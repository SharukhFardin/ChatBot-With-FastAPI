from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def first_app():
    return {"message": "Hello, World!"}


# 