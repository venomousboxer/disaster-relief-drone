from django.urls import path
from . import views
urlpatterns = [
        path('', views.streaminga_index, name="index_sa")
]


