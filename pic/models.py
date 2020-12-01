from django.db import models

# Create your models here.

class Fabricante(models.Model):
	nombre = models.CharField(max_length=42)
	pais = models.CharField(max_length=42)
	sitioweb = models.URLField()

	class Meta:
		verbose_name_plural = "Fabricantes"

	def __str__(self):
		return "%s" % self.nombre

class Productos_Medicinales(models.Model):
	nombre = models.CharField(max_length=100)
	precio = models.CharField(max_length=20)
	caracteristicas = models.TextField()
	imagen = models.ImageField(upload_to='productos')

	class Meta:
		verbose_name_plural = "Productos Medicinales"

	def __str__(self):
		return "%s" % self.nombre

class Semillas(models.Model):
	nombre = models.CharField(max_length=100)
	precio = models.CharField(max_length=20)
	caracteristicas = models.TextField()
	detalles = models.TextField()
	imagen = models.ImageField(upload_to='productos')

	class Meta:
		verbose_name_plural = "Semillas"

	def __str__(self):
		return "%s" % self.nombre



class Suplementos(models.Model):
	nombre = models.CharField(max_length=100)
	precio = models.CharField(max_length=20)
	caracteristicas = models.TextField()
	detalles = models.TextField()
	imagen = models.ImageField(upload_to='productos')

	class Meta:
		verbose_name_plural = "Suplementos"

	def __str__(self):
		return "%s" % self.nombre

class Herramientas(models.Model):
	nombre = models.CharField(max_length=100)
	precio = models.CharField(max_length=20)
	caracteristicas = models.TextField()
	especificiaciones = models.TextField()
	fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
	imagen = models.ImageField(upload_to='productos')

	class Meta:
		verbose_name_plural = "Herramientas"

	def __str__(self):
		return "%s" % self.nombre