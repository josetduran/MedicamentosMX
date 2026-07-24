from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Precio:
    proveedor: str

    presentacion: str

    precio_minimo: float

    precio_maximo: float

    precio_promedio: float

    numero_fuentes: int

    fecha_consulta: datetime

    url: Optional[str] = None