from django.urls import path

from .views import list_eggs, new_egg, update_egg, delete_egg

urlpatterns = [
    path('', list_eggs, name ="egg_list"),
    path('new/', new_egg, name ="egg_new"),
    path('update/<int:id>/', update_egg, name ="egg_update"),
    path('delete/<int:id>/', delete_egg, name ="egg_delete"),

]