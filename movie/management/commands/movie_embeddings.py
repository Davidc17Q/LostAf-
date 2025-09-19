import os
import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie
from openai import OpenAI
from dotenv import load_dotenv


class Command(BaseCommand):   # 👈 esto es lo que Django busca
    help = "Genera y guarda embeddings en la base de datos"

    def handle(self, *args, **kwargs):
        # Cargar API Key
        load_dotenv("openAI.env")
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            self.stdout.write(self.style.ERROR("❌ No se encontró OPENAI_API_KEY"))
            return

        client = OpenAI(api_key=api_key)

        movies = Movie.objects.all()
        self.stdout.write(f"Found {movies.count()} movies in the database")

        for movie in movies:
            if not movie.description:
                continue

            response = client.embeddings.create(
                input=movie.description,
                model="text-embedding-3-small"
            )
            emb = np.array(response.data[0].embedding, dtype=np.float32)
            movie.emb = emb.tobytes()
            movie.save()
            self.stdout.write(f"👌 Embedding stored for: {movie.title}")

        self.stdout.write(self.style.SUCCESS("🌟 Finished generating embeddings for all movies"))
