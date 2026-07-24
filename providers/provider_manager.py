from typing import List

from models.medicamento import Medicamento
from models.precio import Precio
from providers.base import PriceProvider


class ProviderManager:

    def __init__(self):
        self.providers: List[PriceProvider] = []

    def registrar(self, provider: PriceProvider):
        self.providers.append(provider)

    def buscar(self, medicamento: Medicamento) -> List[Precio]:

        resultados = []

        for provider in self.providers:

            try:

                precio = provider.buscar(medicamento)

                if precio is not None:
                    resultados.append(precio)

            except Exception as ex:

                print(f"Error en {provider.__class__.__name__}: {ex}")

        return resultados