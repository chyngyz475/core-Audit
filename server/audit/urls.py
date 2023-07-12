from django.urls import path
from . import views
from .views import GenerateReportAPIView, ExportPdfView


urlpatterns = [
      path('', views.index, name ='core'),
      path('home/', views.HomeView.as_view(), name ='home'),
      path('logout/', views.LogoutView.as_view(), name ='logout'),
      path('restart.html', views.restart_view, name='restart'),
      path('restart1.html', views.restart1_view, name='restart1'),
      path('reference.html', views.reference, name='reference'),
      path('generate-report/', GenerateReportAPIView.as_view(), name='generate_report'),
      path('export_report/', ExportPdfView.as_view({"get":"list"}), name='export_pdf'),
]
