from django.contrib import admin

# Register your models here.
from students.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': (('first_name', 'last_name'), 'middle_name', ('birth_date', 'gender'))
        }),
        ('Course Information', {
            # 'classes': ('collapse',),
            'fields': (('degree', 'department'), ('reg_year', 'reg_no')),
        }),
        ('Graduation Information', {
            # 'classes': ('collapse',),
            'fields': ('pass_year', ),
        }),
    )
    list_display = ['reg_no', 'gender', 'first_name', 'last_name', 'degree', 'department', 'reg_year', 'pass_year']
    list_filter = (
        'gender',
        'degree',
        'department',
        'reg_year',
        'pass_year',
    )
    search_fields = (
        'reg_no',
        'first_name',
        'last_name',
        'pass_year',
    )
    save_as = True
