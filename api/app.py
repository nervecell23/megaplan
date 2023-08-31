from fastapi import FastAPI
from api.utils_controller import route as utils_route

app = FastAPI(title="Hello World business API")

app.include_router(utils_route)
