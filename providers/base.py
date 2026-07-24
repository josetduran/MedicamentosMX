from abc import ABC, abstractmethod

from models.medicamento import Medicamento
from models.precio import Precio


class PriceProvider(ABC):

    @property
    @abstractmethod
    def nombre(self) -> str:
        """Nombre del proveedor."""
        pass

    @abstractmethod
    def buscar(
        self,
        medicamento: Medicamento
    ) -> list[Precio]:
        """Devuelve una lista de precios encontrados."""
        pass