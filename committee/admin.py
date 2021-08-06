from django.contrib import admin

# Register your models here.
from committee.models import CommitteeMember


@admin.register(CommitteeMember)
class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ['position', 'member']
    list_filter = (
        'position',
    )
    search_fields = (
        'position',
        'member__user__first_name',
        'member__user__last_name',
    )
    raw_id_fields = ('member',)
    save_as = True

