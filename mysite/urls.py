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
from django.conf.urls import url
from django.contrib import admin
from .views import Index, UserSite, ActivationUser

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^user/register/', UserSite.as_view(mode=1), name='register'),
    url(r'^user/login/', UserSite.as_view(mode=2), name='login'),
    url(r'^user/logout/', UserSite.as_view(mode=3), name='logout'),
    url(r'^activation/(?P<activationUrl>[0-9]{7,9})/', ActivationUser.as_view(), name='activation')
]
