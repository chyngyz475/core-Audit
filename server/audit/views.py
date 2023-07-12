import os
from platform import python_version
from django.conf import settings
from core.settings import CONNECTION_DB
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from pyreportjasper import PyReportJasper
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from audit.models import Dict
from audit.models import Dict_type
from .forms import DictForm, DictTypeForm
from django.shortcuts import render
from django.http import HttpResponse
import os
from pyreportjasper import PyReportJasper
from platform import python_version
import requests
from django.template.loader import get_template
import jasper
from rest_framework import status
from django.db import connections
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dict
from .serializers import DictSerializer
from pyreportjasper import PyReportJasper
from django.template import loader
from django.http import HttpResponse
import pdfkit

class GenerateReportAPIView(APIView):
    def get(self, request):
        try:
            code = request.GET.get('code', None)
            name = request.GET.get('name', None)
            dict = Dict.objects.filter(code=code, name=name).first()
            
            if not dict :
                return Response({"error_message": "Отчет не найден."}, status=status.HTTP_404_NOT_FOUND)

            # Загрузка шаблона HTML с использованием Jinja2
            template = loader.get_template('report_template.html')
            context = {'dict': dict}
            rendered_html = template.render(context)

            # Генерация PDF из HTML-шаблона с помощью pdfkit
            pdfkit.from_string(rendered_html, 'result.pdf')

            # Отправка PDF-файла в HTTP-ответе
            with open('templates.pdf', 'rb') as fh:
                response = HttpResponse(fh.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename=' + 'output_file.pdf'
                return response

        except:
            return Response({"error_message": "Ошибка!"},  status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        


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

def reference(request: HttpRequest) -> HttpResponse:
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
                  template_name='reference.html',
                  context=context)

class ExportPdfView(viewsets.ViewSet):
    def list(request, self):
        REPORTS_DIR = os.path.join('reports')
        input_file = os.path.join(REPORTS_DIR, 'dict.jrxml')  
        output_file = os.path.join(REPORTS_DIR, 'result')   
        code = None
        name = None

        pyreportjasper = PyReportJasper()
        pyreportjasper.config(
            input_file,
            output_file,
            db_connection=CONNECTION_DB,
            output_formats=["pdf"],  
            parameters={"code": code, "name": name,   'isOnServer': True,},  # Параметры для передачи в отчет
            locale='en_US'  
        )
        pyreportjasper.process_report() 

        file_path = os.path.join(REPORTS_DIR, 'result.pdf')  

        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/pdf")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                os.remove(file_path)  
                return response

