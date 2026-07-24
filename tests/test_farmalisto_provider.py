from providers.farmalisto_provider import FarmalistoProvider
from models.medicamento import Medicamento

provider = FarmalistoProvider()

med = Medicamento(
    laboratorio="Bayer",
    producto="Aspirina"
)

precios = provider.buscar(med)

print("Productos encontrados:", len(precios))

for p in precios[:5]:
    print(
        p.presentacion,
        p.precio_promedio,
        p.url
    )