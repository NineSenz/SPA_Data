from django.urls import path

from frontend import views

urlpatterns = [
    path('add_person/', views.add_person),
    path('show_person/', views.show_person),
]