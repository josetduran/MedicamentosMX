from pathlib import Path
import csv


class LogService:

    def __init__(self):
        Path("logs").mkdir(exist_ok=True)

    def registrar_no_encontrado(
        self,
        laboratorio,
        producto,
        proveedor
    ):
        archivo = Path("logs/no_encontrados.csv")

        existe = archivo.exists()

        with open(
            archivo,
            "a",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            if not existe:
                writer.writerow([
                    "LABORATORIO",
                    "PRODUCTO",
                    "PROVEEDOR"
                ])

            writer.writerow([
                laboratorio,
                producto,
                proveedor
            ])
    
    def registrar_encontrado(
        self,
        laboratorio,
        producto,
        proveedor,
        precio,
        url
    ):
        archivo = Path("logs/encontrados.csv")

        existe = archivo.exists()

        with open(
            archivo,
            "a",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            if not existe:
                writer.writerow([
                    "LABORATORIO",
                    "PRODUCTO",
                    "PROVEEDOR",
                    "PRECIO",
                    "URL"
                ])

            writer.writerow([
                laboratorio,
                producto,
                proveedor,
                precio,
                url
            ])