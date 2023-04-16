from django.urls import path
from .views import AirportList, AirportDetail

urlpatterns = [

    path('airport/',AirportList.as_view()),
    path('airport/<int:pk>/',AirportDetail.as_view())
]