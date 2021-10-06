from django.contrib import admin
from . models import Stock,TradingSignal

class TradingSignalAdmin(admin.ModelAdmin):
    list_display = ("ticker","Direction","EntryDate","ExitDate")

# Register your models here.
admin.site.register(Stock)
admin.site.register(TradingSignal,TradingSignalAdmin)