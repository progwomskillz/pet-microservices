from fastapi import FastAPI

from application.routes import general_router


application = FastAPI()
application.include_router(general_router)
