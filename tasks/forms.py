from django.forms import ModelForm
from django.contrib.auth.hashers import make_password
from .models import Task, Commission, Register_assistence, Vacation_rescheduling, \
    Official_permit_for_hours, Personal_leave_with_pay, Vacation_account_request, Data_user, \
    UsuarioComun, UsuarioAdministrador
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UsuarioSignUpForm(UserCreationForm):
    #user_name = forms.CharField(max_length=25, required=False)
    nombre = forms.CharField(max_length=25, required=False)
    a_paterno = forms.CharField(max_length=15, required=False)
    a_materno = forms.CharField(max_length=15, required=False)
    reparticion = forms.CharField(max_length=10, required=False)
    item = forms.IntegerField(required=False)

    class Meta:
        model = UsuarioComun
        fields = ('username', 'nombre', 'a_paterno', 'a_materno', 'reparticion', 'item', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if UsuarioAdministrador.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está registrado por un usuario de RRHH.")
        return username


class ColaboradorSignUpForm(UserCreationForm):
    #user_name = forms.CharField(max_length=25, required=False)
    nombre = forms.CharField(max_length=25, required=False)
    a_paterno = forms.CharField(max_length=15, required=False)
    a_materno = forms.CharField(max_length=15, required=False)
    item = forms.IntegerField(required=False)
    class Meta:
        model = UsuarioAdministrador
        fields = ('username', 'nombre', 'a_paterno', 'a_materno', 'item', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if UsuarioComun.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está registrado.")
        return username

class SinginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
# class User_RRHHForm(ModelForm):
#     class Meta:
#         model = User_RRHH
#         fields = ['user_name', 'nombre', 'a_paterno', 'a_materno', 'password', 'item']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['reason', 'detail', 'startdate', 'finaldate']


class CommissionForm(ModelForm):
    class Meta:
        model = Commission
        fields = ['unit', 'detail', 'startdate', 'finaldate']


class Register_assistenceForm(ModelForm):
    class Meta:
        model = Register_assistence
        fields = ['date', 'hora_ingreso_mañana', 'hora_salida_mañana', 'hora_ingreso_tarde', 'hora_salida_tarde',
                  'reason', 'constancy']


class Vacation_reschedulingForm(ModelForm):
    class Meta:
        model = Vacation_rescheduling
        fields = ['fecha_programada1_desde', 'fecha_programada1_hasta', 'fecha_programada2_desde',
                  'fecha_programada2_hasta', 'fecha_de_reprogramación1_desde', 'fecha_de_reprogramación1_hasta',
                  'fecha_de_reprogramación2_desde', 'fecha_de_reprogramación2_hasta',
                  'fecha_de_reprogramación3_desde', 'fecha_de_reprogramación3_hasta',
                  'motivos_de_reprogramación', 'justificación_de_la_reprogramación', 'dias_habiles']


class Official_permit_for_hoursForm(ModelForm):
    class Meta:
        model = Official_permit_for_hours
        fields = ['comisión', 'motivo_de_la_comisión', 'fecha_de_salida', 'desde_hora', 'hasta_hora']


class Personal_leave_with_payForm(ModelForm):
    class Meta:
        model = Personal_leave_with_pay
        fields = ['compensación', 'fecha_de_compensación', 'compensación_desde_hora', 'compensación_hasta_hora'
            , 'fecha_de_salida', 'salida_desde_hora', 'salida_hasta_hora']


class Vacation_account_requestForm(ModelForm):
    class Meta:
        model = Vacation_account_request
        fields = ['fecha_de_solicitud', 'fecha_solicitada1', 'fecha_solicitada1_hasta',
                  'fecha_solicitada2', 'fecha_solicitada2_hasta', 'fecha_solicitada3', 'fecha_solicitada3_hasta',
                  'motivo', 'justificación']


class Data_userForm(ModelForm):
    class Meta:
        model = Data_user
        fields = ['nombre', 'a_paterno', 'a_materno', 'reparticion', 'item']
