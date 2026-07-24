from providers.provider_manager import ProviderManager
from providers.mock_provider import MockProvider


class SearchService:

    def __init__(self):
        self.manager = ProviderManager()
        self.manager.registrar(MockProvider())

    def buscar(self, medicamento):
        return self.manager.buscar(medicamento)