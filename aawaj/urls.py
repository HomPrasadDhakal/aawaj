"""
URL configuration for aawaj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from audio import views as audio
from accounts import views as acc
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



schema_view = swagger_get_schema_view(
    openapi.Info(
        title='Documentation for AAwaj APIs',
        default_version='1.0.0',
        description='APIs Documentation from AAwaj APIs',
    ),
    public=True,
)


admin.site.site_header = "Aawaj"
admin.site.index_title = "Welcome to the  Aawaj admin control pannel"

router = DefaultRouter()


router.register(
    "apis/v1/public/audiobooks", audio.AllAudioBooksList, basename="All-audio-books"
),
router.register(
    "apis/v1/public/registration", acc.UserRegistration, basename="user-registration"
),
router.register(
    "apis/v1/impl/registration-email-verify", acc.VerifyEmail, basename="verify_registration_email",
),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path("", include(router.urls)),
    path("apis/v1/impl/user-login/", TokenObtainPairView.as_view(), name="login_view"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh_view"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)