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

            datos.append(
                [
                    m.laboratorio,
                    m.producto,
                    m.presentacion,
                    m.precio_minimo,
                    m.precio_maximo,
                    m.precio_promedio,
                    m.numero_fuentes,
                    m.fecha_consulta,
                ]
            )

        pd.DataFrame(datos, columns=COLUMNAS_SALIDA).to_excel(
            ARCHIVO_SALIDA,
            index=False,
        )