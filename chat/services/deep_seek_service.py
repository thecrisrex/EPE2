import os
import requests

class DeepSeekService:
    def __init__(self):
        self.api_url = os.getenv("DEEPSEEK_API_URL")
        self.api_key = os.getenv("DEEPSEEK_API_KEY")

        print("🔑 API URL:", self.api_url)
        print("🔐 API KEY:", self.api_key)

        self.prompt_template = """
        Analiza los siguientes datos OSINT generados por {source} según los principios de OWASP, buenas prácticas de ciberseguridad y arquitectura segura.

        Datos:
        {data}

        Proporciona un análisis técnico claro y detallado.
        """
