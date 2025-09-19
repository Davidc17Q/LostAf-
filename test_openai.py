import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar las variables de entorno
load_dotenv("openAI.env")

# Verificar si se cargó bien la key
print("API Key:", os.environ.get("openai_apikey"))  # 👈 esto es solo para debug

# Inicializar cliente
client = OpenAI(api_key=os.environ.get("openai_apikey"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Eres un asistente de prueba."},
        {"role": "user", "content": "Hola! Solo dime si esto funciona ✅"}
    ],
)

print(response.choices[0].message.content)
