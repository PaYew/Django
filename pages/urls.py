from django.urls import path
from pages.views import formularz
from . import views

urlpatterns = [
        path("post",views.post, name="post"),
        path("formularz",views.formularz, name="formularz")
        ]

