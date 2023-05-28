from fastapi import FastAPI, Response
from Personas.routes.routes import persona

app = FastAPI(
    title="Personas",
    version="1.0.0.0",
    docs_url = "/api/docs",
    redoc_url= "/api/docs"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(persona, prefix="/api/personas")

