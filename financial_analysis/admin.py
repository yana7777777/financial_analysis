from django.contrib import admin
from .models import FinancialDocument, FinancialRatio


@admin.register(FinancialDocument)
class FinancialDocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'document_type', 'upload_date']
    list_filter = ['document_type', 'upload_date']


@admin.register(FinancialRatio)
class FinancialRatioAdmin(admin.ModelAdmin):
    list_display = ['ratio_name', 'ratio_value', 'document', 'calculation_date']
    list_filter = ['ratio_name']
