from django.db import models

# Create your models here.

class EXPEDIENTE(models.Model):
    anio=models.IntegerField(null=True)
    numeroEntidad=models.IntegerField(null=True)
    descripcionEntidad=models.CharField(max_length=200,null=True)
    expediente=models.IntegerField(null=True)
    codigoTipoOperacion=models.CharField(max_length=40,null=True)
    descripcionTipoOperacion=models.CharField(max_length=200,null=True)
    codigoModalidadCompra=models.CharField(max_length=40,null=True)
    descripcionModalidadCompra=models.CharField(max_length=200,null=True)
    codigoTipoProcesoSeleccion=models.IntegerField(null=True)
    descripcionTipoProceseoSeleccion=models.CharField(max_length=200,null=True)

class DETALLE_EXPEDIENTE(models.Model):
    expediente=models.ForeignKey(EXPEDIENTE,on_delete=models.CASCADE)
    ciclo=models.CharField(max_length=2,null=True)
    fase=models.CharField(max_length=2,null=True)
    sec=models.IntegerField(null=True)
    corr=models.IntegerField(null=True)
    doc=models.CharField(max_length=40,null=True)
    numero=models.CharField(max_length=40,null=True)
    fecha=models.CharField(max_length=40,null=True)
    ff=models.CharField(max_length=40,null=True)
    moneda=models.CharField(max_length=10,null=True)
    monto=models.FloatField(null=True)
    est=models.CharField(max_length=40,null=True)
    fechaProceso=models.CharField(max_length=40,null=True)
    idTrx=models.CharField(max_length=40,null=True)