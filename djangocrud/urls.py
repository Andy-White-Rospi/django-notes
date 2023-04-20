"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from tasks import views
from django.urls import path
from tasks.views import RegistroTipo1, RegistroTipo2
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.RegistroTipo2.as_view(), name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    #path('create_task/', views.registro_de_asistencia, name='create_task'),
    path('commissions/',views.commission, name='commissions'),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('taks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('register_of_assistence/', views.registro_de_asistencia, name='registro_de_asistencia'),
    path('vacation_rescheduling/', views.vacation_rescheduling, name='vacation_rescheduling'),
    path('official_permit_for_hours/', views.official_permit_for_hours, name='official_permit_for_hours'),
    path('personal_leave_with_pay/', views.personal_leave_with_pay, name='personal_leave_with_pay'),
    path('vacation_account_request/', views.vacation_account_request, name='vacation_account_request'),
    path('signup_RRHH/', views.RegistroTipo1.as_view(), name='user_RRHH'),
    # path('signup_RRHH/', views.RegistroTipo1, name='user_RRHH'),
    path('adentro/',views.adentro,name='adentro'),
]
