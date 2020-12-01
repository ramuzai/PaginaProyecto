from django.contrib import admin
from pic.models import *

class FabricanteAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'sitioweb')
	search_fields = ('nombre',)
	ordering = ('nombre',)

class ProdsOneAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'precio')
	search_fields = ('nombre', 'precio')
	ordering = ('nombre',)

class ProdsTwoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'precio', 'fabricante')
	search_fields = ('nombre', 'precio', 'fabricante__nombre')
	ordering = ('nombre',)

admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Productos_Medicinales, ProdsOneAdmin)
admin.site.register(Semillas, ProdsOneAdmin)
admin.site.register(Suplementos, ProdsOneAdmin)
admin.site.register(Herramientas, ProdsTwoAdmin)