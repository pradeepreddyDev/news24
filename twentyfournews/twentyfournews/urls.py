"""lunar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from categories import views as english
from categories_telugu import views as telugu


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', english.index),
    path('detail/<slug:slug>', english.detail),
    path('category/<int:id>', english.category),
    path('gallery/', english.gallery),
    path('videos/', english.videos),
    path('reviews/', english.reviews),
    path('cms/<int:id>', english.cms),
    path('contactus/', english.contactus),
    path('send', english.send),
    path('te', telugu.index),
    path('telugudetail/<slug:slug>', telugu.telugudetail),
    path('telugucategory/<int:id>', telugu.telugucategory),
    path('telugugallery/', telugu.telugugallery),
    path('teluguvideos/', telugu.teluguvideos),
    path('telugureviews/', telugu.telugureviews),
    path('telugucms/<int:id>', telugu.telugucms),
    path('telugucontactus/', telugu.telugucontactus),
    path('tesend', telugu.tesend),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
