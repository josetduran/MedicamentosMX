from typing import List

from models.medicamento import Medicamento
from models.precio import Precio

from providers.base import PriceProvider
from providers.farmalisto_provider import FarmalistoProvider
from providers.benavides_provider import BenavidesProvider
from providers.yza_provider import YzaProvider


class ProviderManager:

    def __init__(self):

        self.providers = [
            FarmalistoProvider(),
            BenavidesProvider(),
            YzaProvider()
        ]

    def registrar(self, provider: PriceProvider):

        self.providers.append(provider)

    def buscar(self, medicamento: Medicamento) -> List[Precio]:

        resultados = []

        for provider in self.providers:

            try:

                precios = provider.buscar(medicamento)

                if precios:
                    resultados.extend(precios)

            except Exception as ex:

                print(f"Error en {provider.nombre}: {ex}")

        return resultados