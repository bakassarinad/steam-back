from django.urls import path
from api import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view()),
    path('categories/<int:id>/', views.category_detailed),
    path('games/', views.GamesView.as_view()),
    path('games/<int:id>/', views.game_details)
]