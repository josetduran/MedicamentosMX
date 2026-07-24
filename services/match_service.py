from rapidfuzz import fuzz


class MatchService:

    def score(self, buscado: str, encontrado: str) -> int:
        return fuzz.token_set_ratio(
            buscado.upper(),
            encontrado.upper()
        )

    def ordenar(self, buscado: str, precios: list):

        precios.sort(
            key=lambda p: self.score(
                buscado,
                p.presentacion
            ),
            reverse=True
        )

        return precios