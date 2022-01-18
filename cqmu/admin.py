from django.contrib import admin
from .models import *
from .widgets import FileFieldWidget
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(TopicCategory)
class TopicCategoryAdmin(admin.ModelAdmin):
    list_display = ('label', 'parent', 'seq')


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('label', 'seq')


@admin.register(WorkUnit)
class WorkUnitAdmin(admin.ModelAdmin):
    list_display = ('label', 'seq')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('big_size_img', 'small_size_img', 'seq')
    readonly_fields = ('big_size_img', 'small_size_img')

    def big_size_img(self, obj):
        return mark_safe('<img src="%s" width="300px;" />' % obj.big_size)

    def small_size_img(self, obj):
        return mark_safe('<img src="%s" width="150px;" />' % obj.small_size)

    big_size_img.short_description = '主题图片-大尺寸'
    small_size_img.short_description = '主题图片-小尺寸'


@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('big_size_img', 'is_open', 'seq')
    readonly_fields = ('big_size_img',)

    def big_size_img(self, obj):
        return mark_safe('<img src="%s" width="300px;" />' % obj.big_size)

    big_size_img.short_description = '首页图片'


@admin.register(FileCategory)
class FileCategoryAdmin(admin.ModelAdmin):
    list_display = ('label', 'form', 'icon_img', 'seq')
    readonly_fields = ('icon_img', )

    def icon_img(self, obj):
        return mark_safe('<img src="%s" width="150px;" />' % obj.icon)

    icon_img.short_description = '文件类型展示图片'


@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('label', 'file_category', 'topic_category', 'grade', 'work_unit', 'downloads', 'comment_scoring',
                    'visits', 'release_date', 'upload_date')
    search_fields = ('label', 'id')
    list_filter = ('file_category', 'topic_category', 'work_unit', 'grade')
    list_display_links = ('label', )
    fieldsets = (
        ('文件类型', {'fields': ('file_category', 'file', 'url')}),
        ('文件信息', {'fields': (('label', 'presenter'), 'description')}),
        ('更多信息', {'fields': ('grade', 'topic_category', 'work_unit', 'release_date')})
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
admin.site.site_title = '课程思政资源库'
admin.site.site_header = '课程思政资源库'
admin.site.index_title = '课程思政资源库'
