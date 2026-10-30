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

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[date]
    observacao: Mapped[str | None] = mapped_column(String(255))
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))

    usuario: Mapped["Usuario"] = relationship(back_populates="treinos")
    series: Mapped[list["Serie"]] = relationship(
        back_populates="treino", cascade="all, delete-orphan"
    )


class Serie(Base):
    __tablename__ = "series"

    id: Mapped[int] = mapped_column(primary_key=True)
    treino_id: Mapped[int] = mapped_column(ForeignKey("treinos.id"))
    exercicio_id: Mapped[int] = mapped_column(ForeignKey("exercicios.id"))
    carga: Mapped[float]
    repeticoes: Mapped[int]
    ordem: Mapped[int]

    treino: Mapped["Treino"] = relationship(back_populates="series")
    exercicio: Mapped["Exercicio"] = relationship(back_populates="series")