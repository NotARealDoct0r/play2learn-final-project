from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review

    # List attributes
    list_display = ['title', 'featured', 'created', 'updated']

    # Allow 'featured' to be edited directly in the list view
    list_editable = ['featured']

    # Optional: Add filters and search
    list_filter = ['featured', 'created']
    search_fields = ['title', 'content']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')

        return ()