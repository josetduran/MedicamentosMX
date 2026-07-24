import requests

from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import quote

from providers.base import PriceProvider
from models.precio import Precio


class FarmalistoProvider(PriceProvider):

    @property
    def nombre(self):
        return "Farmalisto"

    def buscar(self, medicamento):

        url = (
            "https://farmalisto.com.mx/buscar"
            "?controller=search"
            "&order=product.position.desc"
            "&c=0"
            "&s=" + quote(medicamento.producto)
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

        resultados = []

        productos = soup.select("article.product-miniature")

        for producto in productos:

            titulo = producto.select_one(".product-title a")

            nombre = titulo.text.strip()

            if medicamento.producto.upper() not in nombre.upper():
                continue

            precio = producto.select_one(".price")

            if titulo is None or precio is None:
                continue

            texto_precio = (
                precio.text
                .replace("$", "")
                .replace(",", "")
                .strip()
            )

            try:
                valor = float(texto_precio)
            except ValueError:
                continue

            resultados.append(
                Precio(
                    proveedor=self.nombre,
                    presentacion=titulo.text.strip(),
                    precio_minimo=valor,
                    precio_maximo=valor,
                    precio_promedio=valor,
                    numero_fuentes=1,
                    fecha_consulta=datetime.now(),
                    url=titulo["href"],
                )
            )

        return resultados