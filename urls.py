from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('movie.urls')),  # 👈 conecta las urls de tu app movie
]
