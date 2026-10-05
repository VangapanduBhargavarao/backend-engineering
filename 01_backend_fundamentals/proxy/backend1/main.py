from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root(request: Request):
    return {
        "server": "backend-1",
        "message": "Request reached backend 1",
        "client_host": request.client.host if request.client else None
    }


@app.get("/users")
async def users():
    return {
        "server": "backend-1",
        "users": ["Bhargav", "Rahul", "Anil"]
    }


@app.get("/health")
async def health():
    return {
        "server": "backend-1",
        "status": "healthy"
    }