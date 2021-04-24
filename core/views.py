from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import CheckList


class TestAPIView(APIView):
    def get(self, request, format=None):
        return Response({"name": "SKKKKKKK"})


class CheckListsAPIView(APIView):
    def get(self, request, format=None):
        data = CheckList.objects.all()
        return Response(data)
