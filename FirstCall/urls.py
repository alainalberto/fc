"""FirstCall URL Configuration

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
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required

from FirstCall.views import home_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_required(home_view), name='home'),
    url(r'^tools/', include('apps.tools.urls')),
    url(r'^accounting/', include('apps.accounting.urls')),
    url(r'^services/', include('apps.services.urls')),
    url(r'^logistic/', include('apps.logistic.urls')),
    url(r'^accounts/login/', login, {'template_name':'Login/login.html'}, name='login'),

]
