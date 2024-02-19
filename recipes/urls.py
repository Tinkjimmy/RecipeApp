# urls.py in the 'recipes' app
from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, records
from .views import add_recipe

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),  # Assuming you want to use 'home' as the name for the home view
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('recipes/', records, name='records'), 
    path('detail/<int:pk>/', RecipeDetailView.as_view(), name='detail'),
    path('add/', add_recipe, name='add_recipe'),
]
