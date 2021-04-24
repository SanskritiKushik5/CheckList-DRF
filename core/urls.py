from django.urls import path
from core.views import TestAPIView, CheckListsAPIView

urlpatterns = [
    path("", TestAPIView.as_view()),
    path("api/checklists/", CheckListsAPIView.as_view()),
]
