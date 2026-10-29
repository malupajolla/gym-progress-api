from datetime import date
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(150), unique=True)
    senha_hash: Mapped[str] = mapped_column(String(255))

    treinos: Mapped[list["Treino"]] = relationship(back_populates="usuario")


class Exercicio(Base):
    __tablename__ = "exercicios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), unique=True)
    grupo_muscular: Mapped[str] = mapped_column(String(50))

    series: Mapped[list["Serie"]] = relationship(back_populates="exercicio")


class Treino(Base):
    __tablename__ = "treinos"

    id: Mapped[int] =