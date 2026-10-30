from pydantic import BaseModel, ConfigDict


class ExercicioCreate(BaseModel):
    nome: str
    grupo_muscular: str


class ExercicioOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome: str
    grupo_muscular: str