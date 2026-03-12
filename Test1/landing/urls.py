from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name = 'main'),
    path('publication/<int:id>/', views.artViev, name='article_detail'),
]