from fastapi import APIRouter, status
from pydantic import EmailStr
from Personas.model.Persona import FilterPersona
from Personas.routes.functions import *
from fastapi.responses import JSONResponse
persona = APIRouter()

@persona.post(path="/getAll",
              response_description="Obtiene todas las personas.", tags=['Personas'])
async def obtener_personas(correo: EmailStr):
    """A dummy docstring."""
    try:
        return await get_persona(correo)
    except Exception as error:
        result = {'success': False,'detail': error}
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
        
@persona.post(path="/",
              response_description="Registra un Ticket.", tags=['Personas'])
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
