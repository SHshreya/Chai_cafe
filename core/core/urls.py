from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Import views from the current app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),  # Lowercase name for consistency
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('chai/', include('chai.urls')),

    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
