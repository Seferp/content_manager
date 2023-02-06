from django.urls import path
from manager import views

urlpatterns = [
    path('manager', views.manager),
    path('rename_auto', views.rename_auto),
    path('rename_manual', views.rename_manual),
    path('new_direction', views.new_direction),
    path('move', views.move),
    path('remove', views.remove),
    path('search', views.search),
]


