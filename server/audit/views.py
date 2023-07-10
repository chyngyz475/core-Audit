import os
from platform import python_version
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from pyreportjasper import PyReportJasper
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from audit.models import Dict
from audit.models import Dict_type
from .forms import DictForm, DictTypeForm
from django.shortcuts import render
from django.http import HttpResponse
import os
from pyreportjasper import PyReportJasper
from platform import python_version





class HomeView(APIView):
     
   permission_classes = (IsAuthenticated, )
   def get(self, request):
    content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
    return Response(content)
   
class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)
          

def index(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер главной страницы.
    :param request: Объект запроса.
    :return: Объект ответа с главной страницей.
    """
    objects = Dict.objects.using='kazna'
    dict_form = DictForm()
    dict_type_form = DictTypeForm()
    context = {
        "objects":objects,
        'dict_form': dict_form, 'dict_type_form': dict_type_form
    }
    return render(request=request,
                  template_name='index.html',
                  context=context)

def restart_view(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер главной страницы.
    :param request: Объект запроса.
    :return: Объект ответа с главной страницей.
    """

    context = {

    }
    return render(request=request,
                  template_name='restart.html',
                  context=context)

def restart1_view(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер главной страницы.
    :param request: Объект запроса.
    :return: Объект ответа с главной страницей.
    """
    dicts = Dict.objects.using='kazna'
    dict_types = Dict_type.objects.using='kazna'

    context = {
        "dicts": dicts,
        "dict_types": dict_types,
    }
    return render(request=request,
                  template_name='restart1.html',
                  context=context)


