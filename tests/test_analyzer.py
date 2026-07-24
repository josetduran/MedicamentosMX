from services.analyzer_service import AnalyzerService

service = AnalyzerService()

df = service.cargar("logs/no_encontrados.csv")

df = service.clasificar(df)

print(df.head(10))

print()
print("=" * 40)
print("RESUMEN")
print("=" * 40)

print(df["POSIBLE_CAUSA"].value_counts())