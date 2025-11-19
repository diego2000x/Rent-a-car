import json
import requests
from datetime import datetime

class Mindicador:
    def __init__(self, indicador="uf"): # Cambiado a 'uf' por defecto ya que es lo que pide el caso
        self.indicador = indicador

    def obtener_valor_actual(self):
        """
        Obtiene el valor actual del indicador desde la API.
        Si falla la conexión, retorna None para manejar la excepción en el DTO.
        """
        try:
            hoy = datetime.now().strftime("%Y-%m-%d")
            url = f'https://mindicador.cl/api/{self.indicador}'
            response = requests.get(url, timeout=5) # Timeout para evitar bloqueos
            response.raise_for_status() # Lanza error si status no es 200
            
            data = json.loads(response.text.encode("utf-8"))
            
            # Buscamos el valor de hoy
            for item in data["serie"]:
                if item["fecha"].startswith(hoy):
                    return item["valor"]
            
            # Si no hay valor hoy (ej: fin de semana), retorna el más reciente
            if data["serie"]:
                return data["serie"][0]["valor"]
            return 0
            
        except Exception as ex:
            print(f"Error conectando a API: {ex}")
            return None