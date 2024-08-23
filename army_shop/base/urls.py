from django.urls import path

from .views import *

urlpatterns = [
    path("", index),
    path("categories/<int:catid>/", categories),
    path("year/<int:year>/", ageyear)
]
