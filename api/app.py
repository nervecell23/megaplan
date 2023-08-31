from fastapi import FastAPI
from api.utils_controller import route as utils_route

business_app = FastAPI(title="Hello World business API")

business_app.include_router(utils_route)
