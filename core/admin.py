from django.contrib import admin

# Register your models here.
from core.models import MainSector, SubSector, Skills


class SkillsAdmin(admin.ModelAdmin):
    model = Skills

    save_as = True



class MainSectorAdmin(admin.ModelAdmin):
    model = MainSector

    save_as = True


class SubSectorAdmin(admin.ModelAdmin):
    model = SubSector

    save_as = True


admin.site.register(Skills, SkillsAdmin)
admin.site.register(MainSector, MainSectorAdmin)
admin.site.register(SubSector, SubSectorAdmin)
