import pandas as pd

enc = pd.read_csv("logs/encontrados.csv")
no = pd.read_csv("logs/no_encontrados.csv")

enc["CLAVE"] = enc["LABORATORIO"] + "|" + enc["PRODUCTO"]
no["CLAVE"] = no["LABORATORIO"] + "|" + no["PRODUCTO"]

encontrados = set(enc["CLAVE"])
no_encontrados = set(no["CLAVE"]) - encontrados

total = len(encontrados) + len(no_encontrados)

print("=" * 40)
print(f"Medicamentos procesados : {total}")
print(f"Encontrados             : {len(encontrados)}")
print(f"No encontrados          : {len(no_encontrados)}")
print(f"Cobertura               : {len(encontrados)/total:.2%}")
print("=" * 40)