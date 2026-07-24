import requests

from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import quote

from providers.base import PriceProvider
from models.precio import Precio
from services.match_service import MatchService


class BenavidesProvider(PriceProvider):

    @property
    def nombre(self):
        return "Benavides"

    def buscar(self, medicamento):

        url = (
            "https://www.benavides.com.mx/catalogsearch/result/?q="
            + quote(medicamento.producto)
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

        productos = soup.select(".product-item")

        for producto in productos:

            nombre = producto.select_one(".product-item-name")
            precio = producto.select_one(".price-wrapper")

            if nombre is None or precio is None:
                continue

            titulo = nombre.get_text(" ", strip=True)

            if match.score(medicamento.producto, titulo) < 70:
                continue

            try:
                valor = float(
                    precio["data-price-amount"]
                )
            except Exception:
                continue

            enlace = nombre.find("a")

            resultados.append(
                Precio(
                    proveedor=self.nombre,
                    presentacion=titulo,
                    precio_minimo=valor,
                    precio_maximo=valor,
                    precio_promedio=valor,
                    numero_fuentes=1,
                    fecha_consulta=datetime.now(),
                    url=enlace["href"] if enlace else None,
                )
            )

        resultados = match.ordenar(
            medicamento.producto,
            resultados
        )

        return resultados[:3]