import csv

from django.contrib import admin

# Register your models here.


from django.http import HttpResponse

from .models import OficioInterno


@admin.action(description='Exportar para CSV')
def exportar_csv(self, request, queryset):
    opts = self.model._meta

    field_names = [field.name for field in opts.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response


class OficioInternoAdmin(admin.ModelAdmin):
    list_display = ('n_oficio', 'setor', 'destinatario', 'assunto', 'data')
    search_fields = ('n_oficio', 'setor', 'destinatario', 'assunto', 'data')
    list_filter = ['setor']
    actions = [exportar_csv]


admin.site.register(OficioInterno, OficioInternoAdmin)
