from django.urls import path
from crochet_app import views


urlpatterns = [
    path('handmade', views.handmade)

]