from django.contrib import admin
from setscrape.models import *


class SectorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sector, SectorAdmin)


class SymbolAdmin(admin.ModelAdmin):
    pass
admin.site.register(Symbol, SymbolAdmin)


class StockAdmin(admin.ModelAdmin):
    pass
admin.site.register(Stock, StockAdmin)
