from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Exercicio
from app.schemas import ExercicioCreate, ExercicioOut

router = APIRouter(prefix="/exercicios", tags=["Exercícios"])


@router.post("/", response_model=ExercicioOut, status_code=201)
def criar_exercicio(dados: ExercicioCreate, db: Session = Depends(get_db)):
    existente = db.scalar(select(Exercicio).where(Exercicio.nome == dados.nome))
    if existente:
        raise HTTPException(status_code=409, detail="Exercício já cadastrado")

    exercicio = Exercicio(nome=dados.nome, grupo_muscular=dados.grupo_muscular)
    db.add(exercicio)
    db.commit()
    db.refresh(exercicio)
    return exercicio


@router.get("/", response_model=list[ExercicioOut])
def listar_exercicios(db: Session = Depends(get_db)):
    return db.scalars(select(Exercicio)).all()


@router.get("/{exercicio_id}", response_model=ExercicioOut)
def buscar_exercicio(exercicio_id: int, db: Session = Depends(get_db)):
    exercicio = db.get(Exercicio, exercicio_id)
    if not exercicio:
        raise HTTPException(status_code=404, detail="Exercício não encontrado")
    return exercicio