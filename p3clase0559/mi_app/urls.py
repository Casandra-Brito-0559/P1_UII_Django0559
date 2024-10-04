from django.urls import path, include
from mi_app import views
urlpatterns = [
    path('',views.index,name="index"),
    path('Casandra',views.Casandra,name="Casandra"),
    path('minovia',views.minovia,name="minovia")
]