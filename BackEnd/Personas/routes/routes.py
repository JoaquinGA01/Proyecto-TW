from fastapi import APIRouter, status, Request, Form
from pydantic import EmailStr
from Personas.model.Persona import FilterPersona
from Personas.routes.functions import *
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
persona = APIRouter()



@persona.post(path="/getAll",
              response_description="Obtiene todas las personas.", tags=['Personas'])
async def obtener_personas(request: Request,correo: EmailStr = Form(), password: str = Form()):
    """A dummy docstring."""
    try:
        result = await get_persona(correo, password)
        if result.get('success') is False:
            return templates.TemplateResponse("inicio/index.html",{"request":request})
        return templates.TemplateResponse("principal/index.html",{"request":request})
    except Exception as error:
        result = {'success': False,'detail': error}
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
        
@persona.post(path="/registerPersona",
              response_description="Registra una Persona.", tags=['Personas'])
async def crear_persona(persona: Persona):
    """A dummy docstring."""
    try:
        result = await create_persona(persona)
        if result.get('success') is False:
            return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as error:
        result = {'success': False,'detail': error}
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)


