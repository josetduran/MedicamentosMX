import re
import requests

from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import quote

from providers.base import PriceProvider
from models.precio import Precio
from services.match_service import MatchService


class YzaProvider(PriceProvider):

    @property
    def nombre(self):
        return "YZA"

    def buscar(self, medicamento):

        url = (
            "https://www.yza.mx/on/demandware.store/"
            "Sites-YzaMexico-Site/es_MX/Search-UpdateGrid"
            "?q=" + quote(medicamento.producto) +
            "&start=0&sz=12"
        )

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0.0.0 Safari/537.36"
            )
        }

        r = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        if r.status_code != 200:
            return []

        soup = BeautifulSoup(r.text, "html.parser")

        match = MatchService()

        resultados = []

        for producto in soup.select(".product"):

            link = producto.select_one("a.link")

            if link is None:
                continue

            nombre = link.get_text(" ", strip=True)

            if match.score(
                medicamento.producto,
                nombre
            ) < 70:
                continue

            texto = producto.get_text(" ", strip=True)

            m = re.search(
                r"\$ ?([\d,]+\.\d{2})",
                texto
            )

            if not m:
                continue

            valor = float(
                m.group(1).replace(",", "")
            )

            resultados.append(
                Precio(
                    proveedor=self.nombre,
                    presentacion=nombre,
                    precio_minimo=valor,
                    precio_maximo=valor,
                    precio_promedio=valor,
                    numero_fuentes=1,
                    fecha_consulta=datetime.now(),
                    url="https://www.yza.mx" + link["href"],
                )
            )

        resultados = match.ordenar(
            medicamento.producto,
            resultados
        )

        return resultados[:3]