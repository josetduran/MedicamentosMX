import pandas as pd


class AnalyzerService:

    def cargar(self, archivo):

        return pd.read_csv(archivo)

    def clasificar(self, df):

        causas = []

        for _, fila in df.iterrows():

            producto = str(fila["PRODUCTO"]).strip()

            palabras = len(producto.split())

            if len(producto) <= 5:
                causa = "Nombre muy corto"

            elif "MG" not in producto.upper() \
                 and "ML" not in producto.upper() \
                 and "%" not in producto:
                causa = "No contiene dosis"

            elif palabras == 1:
                causa = "Posible nombre comercial"

            elif palabras >= 6:
                causa = "Nombre muy largo"

            else:
                causa = "Revisar manualmente"

            causas.append(causa)

        df["POSIBLE_CAUSA"] = causas

        return df