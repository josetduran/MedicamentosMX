from services.excel_service import ExcelService
from services.search_service import SearchService


class ProcessService:

    def __init__(self):
        self.excel = ExcelService()
        self.search = SearchService()

    def ejecutar(self, callback=None):

        medicamentos = self.excel.leer_medicamentos()

        total = len(medicamentos)

        for indice, medicamento in enumerate(medicamentos, start=1):

            precios = self.search.buscar(medicamento)

            if precios:
                medicamento.precios.extend(precios)

            if callback:
                callback(indice, total, medicamento)

        self.excel.exportar(medicamentos)