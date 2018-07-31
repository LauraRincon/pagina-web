from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Boya

@admin.register(Boya)
class BoyaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'date', 'hour', 'Hs',
                    'Tm02', 'Tp', 'Tz', 'Hm0', 'Hmax', 'H1_10')
