class StatisticsService:

    def calcular(self, medicamentos):

        total = len(medicamentos)

        encontrados = sum(
            1
            for m in medicamentos
            if m.precios
        )

        return {
            "total": total,
            "encontrados": encontrados,
            "no_encontrados": total - encontrados,
            "cobertura": encontrados / total if total else 0
        }