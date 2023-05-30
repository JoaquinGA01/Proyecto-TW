from pydantic import BaseModel, EmailStr
from fastapi import Form
from typing import Optional

class Persona(BaseModel):
    nombre: Optional[str]
    email: EmailStr
    password: str 
    huella: Optional[str]
    
    
class FilterPersona(BaseModel):
    """A dummy docstring."""
    skip: int = 0
    limit: int = 20
    filter: Optional[dict] = {}
    sort_key: Optional[str] = 'created_at'
    sort_direction: Optional[int] = -1    