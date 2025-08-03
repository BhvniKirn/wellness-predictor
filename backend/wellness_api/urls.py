from django.urls import path
from .views import PredictStressView

urlpatterns = [
    path('predict/', PredictStressView.as_view(), name='predict'),
]
