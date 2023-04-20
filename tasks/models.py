from django.db import models
from django.contrib.auth.models import AbstractUser, User, Group, Permission, AbstractBaseUser, PermissionsMixin

#
# Create your models here.
# class Usuario(AbstractBaseUser, PermissionsMixin):
#   email = models.EmailField(unique=True)
#   nombre = models.CharField(max_length=30)
#   apellido = models.CharField(max_length=30)
#   es_activo = models.BooleanField(default=True)
#   es_admin = models.BooleanField(default=False)
#
#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = ['nombre', 'apellido', 'item']
#   groups = models.ManyToManyField(Group, related_name='usuarios_administradores_set')
#   user_permissions = models.ManyToManyField(Permission,verbose_name=('user permissions'),  blank=True, related_name='usuarioadministrador_permissions',  )
#
#   def __str__(self):
#     return self.item
#
#   def get_full_name(self):
#     return f'{self.nombre} {self.apellido}'
#
#   def get_short_name(self):
#     return self.nombre
#
#
# class Funcionario(Usuario):
#   reparticion = models.CharField(max_length=8, unique=True)
#   item = models.CharField(max_length=30)
#
#
# class RRHH(Usuario):
#   item = models.CharField(max_length=30)
class UsuarioComun(AbstractUser):
    # user_name = forms.CharField(max_length=25, null=True, blank=True)
    nombre = models.CharField(max_length=25, null=True, blank=True)
    a_paterno = models.CharField(max_length=15, null=True, blank=True)
    a_materno = models.CharField(max_length=15, null=True, blank=True)
    reparticion = models.CharField(max_length=10, null=True, blank=True)
    item = models.IntegerField(null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='usuarios_comunes_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'), blank=True,
                                              related_name='usuariocomun_permissions', )


class UsuarioAdministrador(AbstractUser):
    # user_name = forms.CharField(max_length=25, null=True, blank=True)
    nombre = models.CharField(max_length=25, null=True, blank=True)
    a_paterno = models.CharField(max_length=15, null=True, blank=True)
    a_materno = models.CharField(max_length=15, null=True, blank=True)
    reparticion = models.CharField(max_length=10, null=True, blank=True)
    item = models.IntegerField(null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='usuarios_administradores_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'), blank=True,
                                              related_name='usuarioadministrador_permissions', )


class Task(models.Model):
    reason = models.CharField(max_length=200)
    detail = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    finaldate = models.DateTimeField(null=True, blank=True)
    startdate = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


class Commission(models.Model):
    reason = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    detail = models.TextField(max_length=1000)
    finaldate = models.DateTimeField(null=True, blank=True)
    startdate = models.DateTimeField(null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


class Register_assistence(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    hora_ingreso_mañana = models.TimeField(verbose_name='Hora del día', null=True, blank=True)
    hora_salida_mañana = models.TimeField(verbose_name='Hora del día', null=True, blank=True)
    hora_ingreso_tarde = models.TimeField(verbose_name='Hora del día', null=True, blank=True)
    hora_salida_tarde = models.TimeField(verbose_name='Hora del día', null=True, blank=True)
    reason = models.CharField(max_length=200, null=True, blank=True)
    constancy = models.CharField(max_length=200, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Vacation_rescheduling(models.Model):
    fecha_programada1_desde = models.DateTimeField(null=True, blank=True)
    fecha_programada1_hasta = models.DateTimeField(null=True, blank=True)
    fecha_programada2_desde = models.DateTimeField(null=True, blank=True)
    fecha_programada2_hasta = models.DateTimeField(null=True, blank=True)
    fecha_de_reprogramación1_desde = models.DateTimeField(null=True, blank=True)
    fecha_de_reprogramación1_hasta = models.DateTimeField(null=True, blank=True)
    fecha_de_reprogramación2_desde = models.DateTimeField(null=True, blank=True)
    fecha_de_reprogramación2_hasta = models.DateTimeField(null=True, blank=True)
    fecha_de_reprogramación3_desde = models.DateTimeField(null=True, blank=True)
    fecha_de_reprogramación3_hasta = models.DateTimeField(null=True, blank=True)
    motivos_de_reprogramación = models.CharField(max_length=200, null=True, blank=True)
    dias_habiles = models.IntegerField(null=True, blank=True)
    justificación_de_la_reprogramación = models.CharField(max_length=500, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Official_permit_for_hours(models.Model):
    comisión = models.CharField(max_length=200, null=True, blank=True)
    motivo_de_la_comisión = models.CharField(max_length=500, null=True, blank=True)
    fecha_de_salida = models.DateTimeField(null=True, blank=True)
    desde_hora = models.TimeField(verbose_name='Hora del día', null=True, blank=True)
    hasta_hora = models.TimeField(verbose_name='Hora del día', null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Personal_leave_with_pay(models.Model):
    compensación = models.CharField(max_length=200, null=True, blank=True)
    fecha_de_compensación = models.DateTimeField(null=True, blank=True)
    compensación_desde_hora = models.TimeField(verbose_name='Hora del día', null=True, blank=True)
    compensación_hasta_hora = models.TimeField(verbose_name='Hora del día', null=True, blank=True)
    fecha_de_salida = models.DateTimeField(null=True, blank=True)
    salida_desde_hora = models.TimeField(verbose_name='Hora del día', null=True, blank=True)
    salida_hasta_hora = models.TimeField(verbose_name='Hora del día', null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


class Vacation_account_request(models.Model):
    fecha_de_solicitud = models.DateTimeField(null=True, blank=True)
    fecha_solicitada1 = models.DateTimeField(null=True, blank=True)
    fecha_solicitada1_hasta = models.DateTimeField(null=True, blank=True)
    fecha_solicitada2 = models.DateTimeField(null=True, blank=True)
    fecha_solicitada2_hasta = models.DateTimeField(null=True, blank=True)
    fecha_solicitada3 = models.DateTimeField(null=True, blank=True)
    fecha_solicitada3_hasta = models.DateTimeField(null=True, blank=True)
    dias_habiles = models.IntegerField(null=True, blank=True)
    motivo = models.CharField(max_length=500, null=True, blank=True)
    justificación = models.CharField(max_length=1000, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


class Data_user(models.Model):
    nombre = models.CharField(max_length=25, null=True, blank=True)
    a_paterno = models.CharField(max_length=15, null=True, blank=True)
    a_materno = models.CharField(max_length=15, null=True, blank=True)
    reparticion = models.CharField(max_length=10, null=True, blank=True)
    item = models.IntegerField(null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

#
# class User_RRHH(models.Model):
#     user_name = models.CharField(max_length=25, null=True, blank=True)
#     nombre = models.CharField(max_length=25, null=True, blank=True)
#     a_paterno = models.CharField(max_length=15, null=True, blank=True)
#     a_materno = models.CharField(max_length=15, null=True, blank=True)
#     password = models.TextField(max_length=500)
#     item = models.IntegerField(null=True, blank=True)
#
#     class Meta:
#         constraints = [models.UniqueConstraint(fields=['user_name'], name='mi_constraint')]


def __str__(self):
    return self.reason + ' - ' + self.user.username
