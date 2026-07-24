import random
from datetime import datetime

from models.precio import Precio
from providers.base import PriceProvider


class MockProvider(PriceProvider):

    @property
    def nombre(self):
        return "MockProvider"

    def buscar(self, medicamento):

        promedio = round(random.uniform(80, 950), 2)

        return [
            Precio(
                proveedor=self.nombre,
                presentacion="Caja con 20 tabletas",
                precio_minimo=round(promedio * 0.95, 2),
                precio_maximo=round(promedio * 1.05, 2),
                precio_promedio=promedio,
                numero_fuentes=random.randint(2, 5),
                fecha_consulta=datetime.now(),
                url=None,
            )
        ]