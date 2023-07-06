from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from audit.models import Dict
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
    context = {
        "objects":objects
    }
    return render(request=request,
                  template_name='index.html',
                  context=context)