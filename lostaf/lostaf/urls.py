from django.urls import path, include  # 👈 Asegúrate de tener include

urlpatterns = [
    path('', include('movie.urls')),  # ✅ Esto es lo único que debe quedarse aquí
]
