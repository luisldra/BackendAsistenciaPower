from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.config import db
from app.models import Student, Group, Attendance
from datetime import date
from app.firebase_config import init_firebase

init_firebase()

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes especificar dominios en lugar de usar "*"
    allow_credentials=True,
    allow_methods=["*"],  # Métodos permitidos: GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Encabezados permitidos
)


# Ruta raíz
@app.get("/")
def read_root():
    return {"message": "API for Basketball Attendance is running"}

# --- ENDPOINTS PARA ESTUDIANTES (STUDENTS) ---

@app.post("/students/")
def create_student(student: Student):
    try:
        # Crear un estudiante
        doc_ref = db.collection("students").document()
        doc_ref.set(student.dict())
        return {"message": "Student created", "id": doc_ref.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/students/")
def get_students():
    try:
        # Obtener todos los estudiantes
        students = db.collection("students").stream()
        return [{"id": s.id, **s.to_dict()} for s in students]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/students/{student_id}/")
def get_student(student_id: str):
    try:
        # Obtener un estudiante por ID
        doc = db.collection("students").document(student_id).get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Student not found")
        return {"id": doc.id, **doc.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/students/{student_id}/")
def update_student(student_id: str, student: Student):
    try:
        # Actualizar estudiante
        doc_ref = db.collection("students").document(student_id)
        doc = doc_ref.get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Student not found")
        doc_ref.update(student.dict())
        return {"message": "Student updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/students/{student_id}/")
def delete_student(student_id: str):
    try:
        # Eliminar estudiante
        doc_ref = db.collection("students").document(student_id)
        doc = doc_ref.get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Student not found")
        doc_ref.delete()
        return {"message": "Student deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --- ENDPOINTS PARA GRUPOS (GROUPS) ---

@app.post("/groups/")
def create_group(group: Group):
    try:
        # Crear un grupo
        if not group.created_at:
            group.created_at = date.today()
        doc_ref = db.collection("groups").document()
        doc_ref.set(group.dict())
        return {"message": "Group created", "id": doc_ref.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/groups/")
def get_groups():
    try:
        # Obtener todos los grupos
        groups = db.collection("groups").stream()
        return [{"id": g.id, **g.to_dict()} for g in groups]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/groups/{group_id}/")
def get_group(group_id: str):
    try:
        # Obtener un grupo por ID
        doc = db.collection("groups").document(group_id).get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Group not found")
        return {"id": doc.id, **doc.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/groups/{group_id}/")
def update_group(group_id: str, group: Group):
    try:
        # Actualizar grupo
        doc_ref = db.collection("groups").document(group_id)
        doc = doc_ref.get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Group not found")
        doc_ref.update(group.dict())
        return {"message": "Group updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/groups/{group_id}/")
def delete_group(group_id: str):
    try:
        # Eliminar grupo
        doc_ref = db.collection("groups").document(group_id)
        doc = doc_ref.get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Group not found")
        doc_ref.delete()
        return {"message": "Group deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --- ENDPOINTS PARA ASISTENCIA (ATTENDANCE) ---

@app.post("/attendance/")
def create_attendance(attendance: Attendance):
    try:
        # Crear registro de asistencia
        doc_ref = db.collection("attendance").document()
        doc_ref.set(attendance.dict())
        return {"message": "Attendance record created", "id": doc_ref.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/attendance/")
def get_attendance():
    try:
        # Obtener todos los registros de asistencia
        attendance = db.collection("attendance").stream()
        return [{"id": a.id, **a.to_dict()} for a in attendance]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/attendance/{attendance_id}/")
def get_attendance_record(attendance_id: str):
    try:
        # Obtener un registro de asistencia por ID
        doc = db.collection("attendance").document(attendance_id).get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Attendance record not found")
        return {"id": doc.id, **doc.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/attendance/{attendance_id}/")
def update_attendance(attendance_id: str, attendance: Attendance):
    try:
        # Actualizar registro de asistencia
        doc_ref = db.collection("attendance").document(attendance_id)
        doc = doc_ref.get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Attendance record not found")
        doc_ref.update(attendance.dict())
        return {"message": "Attendance record updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/attendance/{attendance_id}/")
def delete_attendance(attendance_id: str):
    try:
        # Eliminar registro de asistencia
        doc_ref = db.collection("attendance").document(attendance_id)
        doc = doc_ref.get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Attendance record not found")
        doc_ref.delete()
        return {"message": "Attendance record deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
