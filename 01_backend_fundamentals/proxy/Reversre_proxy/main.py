from fastapi import FastAPI, Request, Response
import httpx

app = FastAPI()

BACKEND_URL = "http://127.0.0.1:8001"


@app.api_route(
    "/{path:path}",
    methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
)
async def reverse_proxy(request: Request, path: str):

    target_url = f"{BACKEND_URL}/{path}"

    body = await request.body()

    headers = dict(request.headers)

    async with httpx.AsyncClient() as client:

        response = await client.request(
            method=request.method,
            url=target_url,
            headers=headers,
            content=body,
            params=request.query_params
        )

    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.headers.get("content-type")
    )