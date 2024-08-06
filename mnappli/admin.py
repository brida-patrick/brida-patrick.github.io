from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display= ('title','quantity','Author')
    list_filter = ['Author','title']
    search_fields = ['title']


admin.site.register(Author)
