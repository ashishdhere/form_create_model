from django.urls import path
from app import views

urlpatterns = [
    path('',views.home),
    path('login/',views.login,name='login'),
    path('data/',views.data,name='data'),
    path('base/',views.base,name='base'),
    path('delete/<int:id>/',views.delete),
    path('<int:id>/',views.update),
    
]
