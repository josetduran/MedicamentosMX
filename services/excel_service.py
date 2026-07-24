import pandas as pd

from config import (
    ARCHIVO_ENTRADA,
    ARCHIVO_SALIDA,
    COLUMNAS_SALIDA,
    RESULTADOS_DIR,
)

from models.medicamento import Medicamento


class ExcelService:

    def leer_medicamentos(self):

        df = pd.read_excel(ARCHIVO_ENTRADA)

        medicamentos = []

        for _, fila in df.iterrows():

            medicamentos.append(
                Medicamento(
                    laboratorio=str(fila["LABORATORIO"]).strip(),
                    producto=str(fila["PRODUCTO"]).strip(),
                )
            )

        return medicamentos

    def exportar(self, medicamentos):

        RESULTADOS_DIR.mkdir(exist_ok=True)

        datos = []

        for m in medicamentos:

            if m.precios:
                primer_precio = m.precios[0]

                presentacion = primer_precio.presentacion
                fecha_consulta = primer_precio.fecha_consulta.strftime(
                    "%Y-%m-%d %H:%M"
                )
            else:
                presentacion = ""
                fecha_consulta = ""

            datos.append(
                [
                    m.laboratorio,
                    m.producto,
                    presentacion,
                    m.precio_minimo,
                    m.precio_maximo,
                    m.precio_promedio,
                    len(m.precios),
                    fecha_consulta,
                ]
            )

        df = pd.DataFrame(
            datos,
            columns=COLUMNAS_SALIDA,
        )

        df.to_excel(
            ARCHIVO_SALIDA,
            index=False,
        )