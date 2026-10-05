from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root(request: Request):
    return {
        "server": "backend-2",
        "message": "Request reached backend 2",
        "client_host": request.client.host if request.client else None
    }


@app.get("/users")
async def users():
    return {
        "server": "backend-2",
        "users": ["Kiran", "Suresh", "Ravi"]
    }


@app.get("/health")
async def health():
    return {
        "server": "backend-2",
        "status": "healthy"
    }