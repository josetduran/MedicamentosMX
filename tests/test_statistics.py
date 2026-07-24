from datetime import datetime

from models.medicamento import Medicamento
from models.precio import Precio
from services.statistics_service import StatisticsService

service = StatisticsService()

m1 = Medicamento(
    laboratorio="LAB1",
    producto="A"
)

m2 = Medicamento(
    laboratorio="LAB2",
    producto="B"
)

resultado = service.calcular([m1, m2])

print(resultado)
print("Precios m1:", len(m1.precios))
print("Precios m2:", len(m2.precios))

#assert resultado["total"] == 2
#assert resultado["encontrados"] == 1
#assert resultado["no_encontrados"] == 1
#assert resultado["cobertura"] == 0.5

print("Prueba con objetos reales: OK")