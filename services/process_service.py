from services.excel_service import ExcelService
from services.search_service import SearchService
from services.log_service import LogService

class ProcessService:

    def __init__(self):
        self.excel = ExcelService()
        self.search = SearchService()
        self.log = LogService()

    def ejecutar(self, callback=None):

        medicamentos = self.excel.leer_medicamentos()

        total = len(medicamentos)

        for indice, medicamento in enumerate(medicamentos, start=1):

            precios = self.search.buscar(medicamento)

            if precios:

                medicamento.precios.extend(precios)

                for precio in precios:

                    self.log.registrar_encontrado(
                        medicamento.laboratorio,
                        medicamento.producto,
                        precio.proveedor,
                        precio.precio_promedio,
                        precio.url
                    )
            else:
                self.log.registrar_no_encontrado(
                    medicamento.laboratorio,
                    medicamento.producto,
                    "Farmalisto"
                )

            if callback:
                callback(indice, total, medicamento)

        self.excel.exportar(medicamentos)