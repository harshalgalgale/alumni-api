from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser", "last_login"]
    search_fields = ["name", "username", "email"]


admin.site.register(User, UserAdmin)
