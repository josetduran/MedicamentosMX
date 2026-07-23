from dataclasses import dataclass

@dataclass
class Medicamento:
    laboratorio: str
    producto: str

    presentacion: str = ""
    precio_minimo: float | None = None
    precio_maximo: float | None = None
    precio_promedio: float | None = None
    numero_fuentes: int = 0
    fecha_consulta: str = ""