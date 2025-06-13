import asyncio
from typing import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    yield


app = FastAPI(lifespan=lifespan, default_response_class=ORJSONResponse, title="Ping", debug=False, docs_url="/api/openapi", openapi_url="/api/openapi.json")


@app.get("/api/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/ping")
async def ping():
    return {"message": "pong"}


@app.get("/api/wait")
async def wait():
    await asyncio.sleep(0.2)
    return {"message": "done"}


if __name__ == "__main__":
    app()




