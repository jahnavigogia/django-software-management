from django.contrib import admin
from .models import Software


# Register your models here.
class Software_det(admin.ModelAdmin):
    list_display = ('name', 'version', 'license', 'user', 'owner', )
    list_filter = ('version', 's_accessible_by_all',)
    search_fields = ('name', 'version', 's_accessible_by_all')

    def get_queryset(self, request):
        # Get the base queryset
        queryset = super().get_queryset(request)

        # Custom logic based on user permissions
        if request.user.is_superuser:
            # Superusers can see all elements
            return queryset
        else:
            # For other users, apply your custom logic
            # For example, restrict based on a field 'owner' in YourModel
            return queryset.filter(owner=request.user)


admin.site.register(Software, Software_det)

