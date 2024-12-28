import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse


def create_http_controller() -> FastAPI:
    api = FastAPI()

    @api.get("/")
    def health() -> JSONResponse:
        return JSONResponse({"result": "OK"})

    @api.get("/greeting/{name}")
    def greeting(name: str) -> JSONResponse:
        return JSONResponse({"result": f"Hello {name}!"})

    return api


def main() -> None:
    http_controller = create_http_controller()

    uvicorn.run(http_controller, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
