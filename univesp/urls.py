
from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('form/', views.form, name='form' ),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.form, name='form'),
    path('about/', views.about, name='about'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
