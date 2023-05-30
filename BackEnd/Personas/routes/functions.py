from Personas.config.db_connection import cluster
from Personas.model.Persona import Persona, FilterPersona
from Personas.tools.paggination import paggination
from bson.objectid import ObjectId
db = cluster["Personas"]
collection_Personas = db["Info"]


async def get_persona(email:str, password: str):
    """A dummy docstring."""
    try:
        metadata = collection_Personas.find_one({'email':email})
        if (metadata != None):
            if(metadata['password'] == password):
                success_descripcion = {'success': True,'detail': 'Persona encontrada'}
            else:
                success_descripcion = {'success': False,'detail': 'Persona no encontrada'}
        else:
            success_descripcion = {'success': False,'detail': 'Persona no encontrada'}
        return success_descripcion
    except Exception as error:
        error_description = {'success': False, 'detail': f'Ha ocurrido un error en get_persona. Error {error}'}
        return error_description
    
async def create_persona(persona_data:Persona):
    """A dummy docstring."""
    print(type(persona_data))
    print(type(persona_data.dict()))
    try:
        insert_persona = collection_Personas.insert_one(persona_data.dict())
        ticket_id = str(insert_persona.inserted_id)
        success_descripcion = {'success': True,'detail': 'Se ha registrado la Persona.',
                'persona_id': ticket_id}
        return success_descripcion
    except Exception as error:
        error_description = {'success': False,'detail': f'Ha ocurrido un error en create_persona. Error {error}'}
        return error_description
