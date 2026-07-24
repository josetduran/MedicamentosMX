from providers.yza_provider import YzaProvider
from models.medicamento import Medicamento

provider = YzaProvider()

med = Medicamento(
    laboratorio="BAYER",
    producto="Aspirina"
)

precios = provider.buscar(med)

print("Productos encontrados:", len(precios))

for p in precios:
    print(
        p.presentacion,
        p.precio_promedio,
        p.url
    )