# marksapp/admin.py
from django.contrib import admin
from .models import Session, Student, Marks, CoScholasticActivity, CoScholasticGrade
from .models import *

@admin.register(ClassSection)
class ClassSectionAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'section']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(CoScholasticActivity)
class CoScholasticActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter  = ['category']


@admin.register(CoScholasticGrade)
class CoScholasticGradeAdmin(admin.ModelAdmin):
    list_display = ['student', 'activity', 'term1_grade', 'term2_grade']
    list_filter  = ['activity__category', 'term1_grade', 'term2_grade']
    search_fields = ['student__name', 'activity__name']
    

admin.site.register([Session, Student, Marks])