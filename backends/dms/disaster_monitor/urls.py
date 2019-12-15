from django.urls import path
from . import views
urlpatterns = [
        path('', views.disaster_index, name="index_dis")
]


