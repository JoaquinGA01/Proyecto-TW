from pydantic import BaseModel, EmailStr
from fastapi import Form
from typing import Optional

class Persona(BaseModel):
    nombre: str
    email: EmailStr
    password: str 
    huella: str 
    
    
class FilterPersona(BaseModel):
    """A dummy docstring."""
    skip: int = 0
    limit: int = 20
    filter: Optional[dict] = {}
    sort_key: Optional[str] = 'created_at'
    sort_direction: Optional[int] = -1    