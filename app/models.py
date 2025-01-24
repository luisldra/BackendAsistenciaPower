from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import date

# Modelo para Estudiantes
class Student(BaseModel):
    id: Optional[str] = Field(default=None, description="ID único del estudiante")
    full_name: str = Field(..., description="Nombre completo del estudiante")
    birth_date: date = Field(..., description="Fecha de nacimiento del estudiante")
    photo_url: Optional[str] = Field(default=None, description="URL de la foto del estudiante")
    contact_number: str = Field(..., description="Número de contacto del estudiante")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "123",
                "full_name": "John Doe",
                "birth_date": "2010-05-12",
                "photo_url": "https://example.com/photo.jpg",
                "contact_number": "1234567890",
            }
        }


# Modelo para Grupos
class Group(BaseModel):
    id: Optional[str] = Field(default=None, description="ID único del grupo")
    name: str = Field(..., description="Nombre del grupo")
    schedule: Dict[str, str] = Field(..., description="Horario del grupo")
    created_at: Optional[date] = Field(default=None, description="Fecha de creación del grupo")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "456",
                "name": "Junior Team",
                "schedule": {"Monday": "5-6 PM", "Wednesday": "6-7 PM"},
                "created_at": "2025-01-24",
            }
        }


# Modelo para Asistencia
class Attendance(BaseModel):
    id: Optional[str] = Field(default=None, description="ID único del registro de asistencia")
    student_id: str = Field(..., description="ID del estudiante")
    group_id: str = Field(..., description="ID del grupo")
    attendance_date: date = Field(..., description="Fecha de la asistencia")
    status: str = Field(..., description="Estado de asistencia ('Presente', 'Ausente', 'Tarde')")
    note: Optional[str] = Field(default=None, description="Notas adicionales")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "789",
                "student_id": "123",
                "group_id": "456",
                "date": "2025-01-23",
                "status": "Present",
                "note": "Llegó tarde",
            }
        }
