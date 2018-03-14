from django.contrib import admin
from .models import ColourCombo

class ColourComboAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at',)

admin.site.register(ColourCombo, ColourComboAdmin)