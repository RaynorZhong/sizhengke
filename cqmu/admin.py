from django.contrib import admin
from .models import *
from .widgets import FileFieldWidget


# Register your models here.
@admin.register(TopicCategory)
class TopicCategoryAdmin(admin.ModelAdmin):
    list_display = ('label', 'parent', 'seq')


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('label', 'seq')


@admin.register(FileCategory)
class FileCategoryAdmin(admin.ModelAdmin):
    list_display = ('label', 'form', 'seq')


@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('label', 'file_category', 'topic_category', 'grade', 'visits', 'downloads', 'comment_scoring',
                    'data_source', 'release_date', 'upload_date')
    search_fields = ('label', 'id')
    list_filter = ('file_category', 'topic_category', 'grade')
    list_display_links = ('label', )
    fieldsets = (
        ('文件类型', {'fields': ('file_category', 'file', 'url')}),
        ('文件信息', {'fields': (('label', 'author', 'presenter'), 'description')}),
        ('更多信息', {'fields': (('grade', 'topic_category'), ('recommended_tag', 'data_source'), 'release_date')})
    )
    formfield_overrides = {
        models.FileField: {'widget': FileFieldWidget},
    }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('file_upload', 'nickname', 'label', 'scoring', 'comment_date')
    list_filter = ('file_upload__label', 'scoring')
    list_display_links = ('file_upload', )
    autocomplete_fields = ('file_upload',)


# admin site
admin.site.site_title = '思想政治资源数据库系统'
admin.site.site_header = '思政数据库'
admin.site.index_title = '思政数据库'
