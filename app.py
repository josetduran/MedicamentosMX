from services.excel_service import ExcelService
from utils.logger import logger

def main():

    logger.info("Inicio del programa")

    excel = ExcelService()

    medicamentos = excel.leer_medicamentos()

    print(f"Medicamentos encontrados: {len(medicamentos)}")

    excel.exportar(medicamentos)

    logger.info("Archivo exportado correctamente")

if __name__ == "__main__":
    main()