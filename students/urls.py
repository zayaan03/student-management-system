from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list,  name = 'student_list'),
    path('add/', views.student_add, name = 'student_add'),
    path('edit/<int:id>/', views.student_edit, name = 'student_edit'),
    path('edit/<int:id>/form/', views.student_edit_form, name = 'student_edit_form'),
    path('delete/<int:id>/', views.student_delete, name= 'student_delete'),
    path('export/csv/', views.export_csv, name='export_csv'),
    path('export/txt/', views.export_txt, name='export_txt'),

]