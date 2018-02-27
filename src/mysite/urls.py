"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from rest_framework.authtoken import views as views_authtoken
from rest_framework.schemas import get_schema_view
from rest_framework_raml.renderers import RAMLRenderer, RAMLDocsRenderer
from rest_framework_swagger.views import get_swagger_view
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'news', views.NewViewSet)

swagger_view = get_swagger_view(title='Pastebin API')

raml_view = get_schema_view(
    title='Example API',
    renderer_classes=[RAMLRenderer, RAMLDocsRenderer]
)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^token-login/', views_authtoken.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^swagger/$', swagger_view),
    url(r'^raml/$', raml_view)
]