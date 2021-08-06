from django.contrib import admin

# Register your models here.
from careers.models import CompanyAddress, Company, JobAdvert


class CompanyAddressInlineAdmin(admin.StackedInline):
    model = CompanyAddress
    extra = 0


@admin.register(CompanyAddress)
class CompanyAddressAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Company Information', {
            'fields': ('company',)
        }),
        ('Company Address', {
            'fields': (
                ('country', 'state'),
                ('district', 'town_city'),
                ('street_name', 'address_line'),
                ('post_code', 'plus_code'),
                )
        }),
    )
    list_display = ['company', 'town_city', 'state', 'country', 'post_code']
    save_as = True


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = (
        CompanyAddressInlineAdmin,
    )


@admin.register(JobAdvert)
class JobAdvertAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Job Information',{
            'fields': (('company_location', 'url'),('title', 'employment_type'), 'description', 'responsibilities')
        }),
        ('Requirements, Perks, Dates and Contact',{
            'fields': (('min_experience', 'min_qualification'),('min_salary', 'max_salary'),('last_date', 'owner'))
        }),
    )
    list_display = ['title', 'company_location', 'last_date', 'min_qualification', 'min_salary']
    save_as = True
