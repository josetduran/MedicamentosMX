from providers.base import BaseProvider
from models.precio import Precio


class GuadalajaraProvider(BaseProvider):

    nombre = "Farmacias Guadalajara"

    def buscar(self, medicamento):
        ...