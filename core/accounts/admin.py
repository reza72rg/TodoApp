from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User, Profile


class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_active", "is_verified")
    list_filter = ("email", "is_staff", "is_active", "is_verified")
    searching_fileds = ("email",)
    ordering = ("email",)
    fieldsets = (
        ("Main", {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                )
            },
        ),
        ("group permissions", {"fields": ("groups", "user_permissions")}),
        ("important date", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                )
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
