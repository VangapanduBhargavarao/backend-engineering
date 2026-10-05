from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import Response
import httpx

app = FastAPI()


@app.api_route(
    "/proxy",
    methods=["GET", "POST", "PUT", "PATCH", "DELETE"]
)
async def forward_proxy(request: Request):

    target_url = request.query_params.get("url")

    if not target_url:
        raise HTTPException(
            status_code=400,
            detail="Missing target URL"
        )

    body = await request.body()

    headers = dict(request.headers)

    headers.pop("host", None)

    async with httpx.AsyncClient() as client:

        response = await client.request(
            method=request.method,
            url=target_url,
            headers=headers,
            content=body
        )

    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.headers.get("content-type")
    )