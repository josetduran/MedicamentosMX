from providers.provider_manager import ProviderManager


class SearchService:

    def __init__(self):
        self.manager = ProviderManager()

    def buscar(self, medicamento):
        return self.manager.buscar(medicamento)