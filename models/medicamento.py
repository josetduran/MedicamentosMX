from dataclasses import dataclass, field

from models.precio import Precio


@dataclass
class Medicamento:
    laboratorio: str
    producto: str

    precios: list[Precio] = field(default_factory=list)

    @property
    def precio_minimo(self):
        if not self.precios:
            return None
        return min(p.precio_promedio for p in self.precios)

    @property
    def precio_maximo(self):
        if not self.precios:
            return None
        return max(p.precio_promedio for p in self.precios)

    @property
    def precio_promedio(self):
        if not self.precios:
            return None

        return round(
            sum(p.precio_promedio for p in self.precios)
            / len(self.precios),
            2,
        )