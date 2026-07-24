from providers.benavides_provider import BenavidesProvider
from models.medicamento import Medicamento

provider = BenavidesProvider()

provider.buscar(
    Medicamento(
        laboratorio="BAYER",
        producto="Aspirina"
    )
)