from django.core.management.base import BaseCommand
from movie.models import Movie
from openai import OpenAI
import os
from dotenv import load_dotenv
from django.core.files.base import ContentFile
import base64


class Command(BaseCommand):
    help = "Genera una imagen para la primera película usando OpenAI"

    def handle(self, *args, **kwargs):
        # Cargar variables de entorno
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            self.stdout.write(self.style.ERROR("❌ No se encontró la OPENAI_API_KEY en el .env"))
            return

        client = OpenAI(api_key=api_key)

        # Buscar la primera película
        movie = Movie.objects.first()
        if not movie:
            self.stdout.write(self.style.ERROR("❌ No hay películas en la BD"))
            return

        # Generar imagen con OpenAI
        prompt = f"Genera un póster artístico para la película '{movie.title}'"
        self.stdout.write(f"🎨 Generando imagen para: {movie.title}")

        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="512x512"
        )

        image_base64 = response.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)

        # Guardar en el campo image del modelo
        movie.image.save(f"{movie.title}_poster.png", ContentFile(image_bytes), save=True)

        self.stdout.write(self.style.SUCCESS(f"✅ Imagen generada y guardada para {movie.title}"))
