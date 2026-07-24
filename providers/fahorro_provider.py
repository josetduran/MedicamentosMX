from providers.base import BaseProvider


class FAhorroProvider(BaseProvider):

    @property
    def nombre(self):
        return "Farmacias del Ahorro"

    def buscar(self, medicamento):
        return []