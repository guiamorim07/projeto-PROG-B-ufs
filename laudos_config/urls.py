"""
URL configuration for laudos_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from laudos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("templates/", views.Templates, name= "templates"), #endpoint para a página de templates GET/POST/PUT
    path("exames/", views.manipular_exame, name= "manipular-exame"), #endpoint para salvar e confirmar laudos POST, abrir laudos GET, atualizar laudos PUT
    path("pacientes/<int:paciente_id>/exames/", views.Consultar_laudos_por_paciente, name= "laudos"), #endpoint para consultar laudos por paciente GET
    path("exames/<int:exame_id>/", views.Listar_exame_especifico, name= "Listar-exame-específico"), #endpoint para listar exame específico GET
    path("cadastro-paciente-medico/", views.Cadastro_Paciente_Medico, name= "Cadastro-Paciente-Medico") #endpoint para cadastrar novo paciente POST
]

