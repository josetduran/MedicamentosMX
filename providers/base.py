from abc import ABC, abstractmethod

from models.medicamento import Medicamento
from models.precio import Precio


class PriceProvider(ABC):

    @abstractmethod
    def buscar(self, medicamento: Medicamento) -> Precio:
        """Busca el precio de un medicamento."""
        pass