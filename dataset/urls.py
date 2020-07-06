from django.urls import path
from dataset.views.Data import Data
from dataset.views.CurrentData import CurrentData
urlpatterns = [
    path('get/data', Data.as_view()),
    path('get/current/data', CurrentData.as_view()),
]
