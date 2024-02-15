# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Empleado(models.Model):

    #__Empleado_FIELDS__
    cedula = models.CharField(max_length=255, null=True, blank=True)
    seg_social = models.CharField(max_length=255, null=True, blank=True)
    nro_empleado = models.CharField(max_length=255, null=True, blank=True)
    foto = models.CharField(max_length=255, null=True, blank=True)
    nombre1 = models.CharField(max_length=255, null=True, blank=True)
    nombre2 = models.CharField(max_length=255, null=True, blank=True)
    apellido1 = models.CharField(max_length=255, null=True, blank=True)
    apellido2 = models.CharField(max_length=255, null=True, blank=True)
    nro_cargo = models.CharField(max_length=255, null=True, blank=True)
    hora_trabajo = models.CharField(max_length=255, null=True, blank=True)
    mes_prueba = models.CharField(max_length=255, null=True, blank=True)

    #__Empleado_FIELDS__END

    class Meta:
        verbose_name        = _("Empleado")
        verbose_name_plural = _("Empleado")


class Contrato(models.Model):

    #__Contrato_FIELDS__
    descrip_contrato = models.CharField(max_length=255, null=True, blank=True)

    #__Contrato_FIELDS__END

    class Meta:
        verbose_name        = _("Contrato")
        verbose_name_plural = _("Contrato")


class Sexo(models.Model):

    #__Sexo_FIELDS__
    descrip_sexo = models.CharField(max_length=255, null=True, blank=True)

    #__Sexo_FIELDS__END

    class Meta:
        verbose_name        = _("Sexo")
        verbose_name_plural = _("Sexo")


class Estadoempleado(models.Model):

    #__Estadoempleado_FIELDS__
    cod_estado = models.CharField(max_length=255, null=True, blank=True)
    descrip_estado = models.CharField(max_length=255, null=True, blank=True)

    #__Estadoempleado_FIELDS__END

    class Meta:
        verbose_name        = _("Estadoempleado")
        verbose_name_plural = _("Estadoempleado")


class Cargo(models.Model):

    #__Cargo_FIELDS__
    cod_cargo = models.CharField(max_length=255, null=True, blank=True)
    descrip_cargo = models.CharField(max_length=255, null=True, blank=True)

    #__Cargo_FIELDS__END

    class Meta:
        verbose_name        = _("Cargo")
        verbose_name_plural = _("Cargo")


class Tiposalario(models.Model):

    #__Tiposalario_FIELDS__
    cod_tipo_salario = models.CharField(max_length=255, null=True, blank=True)
    descrip_tipo_salario = models.CharField(max_length=255, null=True, blank=True)

    #__Tiposalario_FIELDS__END

    class Meta:
        verbose_name        = _("Tiposalario")
        verbose_name_plural = _("Tiposalario")



#__MODELS__END
