from django.urls import path
from . import views

urlpatterns = [
    path('financial_analysis/', views.financial_analysis_page, name='financial_analysis_page'),  # Новая страница
    path('upload/', views.upload_document, name='financial_upload'),
    path('results/<int:document_id>/', views.financial_results, name='financial_results'),
    path('list/', views.document_list, name='financial_list'),
    path('debug/<int:document_id>/', views.debug_document, name='financial_debug'),
]