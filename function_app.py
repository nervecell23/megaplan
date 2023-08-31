import azure.functions as func
from api.app import business_app


app = func.AsgiFunctionApp(app=business_app, http_auth_level=func.AuthLevel.ANONYMOUS)
