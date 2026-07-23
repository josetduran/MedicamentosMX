from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
RESULTADOS_DIR = BASE_DIR / "resultados"
CACHE_DIR = BASE_DIR / "cache"
LOGS_DIR = BASE_DIR / "logs"

ARCHIVO_ENTRADA = DATA_DIR / "Productos.xlsx"
ARCHIVO_SALIDA = RESULTADOS_DIR / "Precios_Medicamentos_MX.xlsx"
LOG_FILE = LOGS_DIR / "medicamentos.log"

COLUMNAS_SALIDA = [
    "LABORATORIO",
    "PRODUCTO",
    "PRESENTACION",
    "PRECIO_MINIMO",
    "PRECIO_MAXIMO",
    "PRECIO_PROMEDIO",
    "NUMERO_FUENTES",
    "FECHA_CONSULTA",
]