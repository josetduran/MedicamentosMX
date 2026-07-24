from services.excel_service import ExcelService
from services.search_service import SearchService
from services.log_service import LogService
from pathlib import Path

class ProcessService:

    def __init__(self):
        self.excel = ExcelService()
        self.search = SearchService()
        self.log = LogService()

    def ejecutar(self, archivo_excel, callback=None):
        Path("logs/encontrados.csv").unlink(missing_ok=True)
        Path("logs/no_encontrados.csv").unlink(missing_ok=True)

        medicamentos = self.excel.leer_medicamentos(archivo_excel)

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
            encontrados = 0

            for medicamento in medicamentos:

                if medicamento.precios:
                    encontrados += 1

            no_encontrados = len(medicamentos) - encontrados

            print()
            print("=" * 40)
            print(f"Medicamentos procesados : {len(medicamentos)}")
            print(f"Encontrados             : {encontrados}")
            print(f"No encontrados          : {no_encontrados}")
            print(f"Cobertura               : {encontrados/len(medicamentos):.2%}")
            print("=" * 40)
        self.excel.exportar(medicamentos)