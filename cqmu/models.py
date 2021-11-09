from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from simplepro.components import fields
from django.db.models import Avg
from django.db import models
from .storage import CosStorage
from django.dispatch import receiver

# Create your models here.


class TopicCategory(models.Model):
    label = fields.CharField(verbose_name='类别主题', max_length=200)
    parent = fields.ForeignKey(verbose_name='上级分类', to='self', null=True, blank=True, on_delete=models.SET_NULL)
    seq = fields.IntegerField(verbose_name='排序序号', default=0)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = '类别主题'
        verbose_name_plural = verbose_name
        ordering = ('seq',)


class Grade(models.Model):
    label = fields.CharField(verbose_name='级别', max_length=200)
    seq = fields.IntegerField(verbose_name='排序序号', default=0)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = '级别'
        verbose_name_plural = verbose_name
        ordering = ('seq',)


class WorkUnit(models.Model):
    label = fields.CharField(verbose_name='所在单位', max_length=200)
    seq = fields.IntegerField(verbose_name='排序序号', default=0)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = '所在单位'
        verbose_name_plural = verbose_name
        ordering = ('seq',)


class FileCategory(models.Model):
    FormList = [
        (1, '超链接'),
        (2, '文件[doc|docx|ppt|pptx|pdf]-下载按钮'),
        (3, '图片[jpg|jpeg|png|bmp]-下载按钮'),
        (4, '音频[mp3]-下载按钮'),
        (5, '视频[mp4]-下载按钮')]

    label = fields.CharField(verbose_name='文件类型', max_length=200)
    form = fields.IntegerField(verbose_name='展现形式', default=1, choices=FormList)
    icon = models.URLField('文件类型展示图片')
    seq = fields.IntegerField(verbose_name='排序序号', default=0)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = '文件类型'
        verbose_name_plural = verbose_name
        ordering = ('seq',)


class FileUpload(models.Model):
    SuffixList = {
        1: None,
        2: ['doc', 'docx', 'ppt', 'pptx', 'pdf'],
        3: ['jpg', 'jpeg', 'png', 'bmp'],
        4: ['mp3'],
        5: ['mp4']
    }

    options1 = """
    {
          disabledDate(time) {
            return time.getTime() > Date.now();
          },
          shortcuts: [{
            text: '今天',
            onClick(picker) {
              picker.$emit('pick', new Date());
            }
          }, {
            text: '昨天',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24);
              picker.$emit('pick', date);
            }
          }, {
            text: '一周前',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', date);
            }
          }]
        }
    """

    label = fields.CharField(verbose_name='文件名', max_length=200)
    file = models.FileField('文件', storage=CosStorage(), help_text='文件大小不超过30MB', max_length=200, blank=True, null=True)
    url = models.URLField('URL', help_text='文件类型的展现形式为超链接，本字段必填', blank=True, null=True)
    presenter = fields.CharField(verbose_name='人物名字', max_length=200)
    description = fields.CharField(verbose_name='事件描述', input_type='textarea', max_length=200, style='width:500px;', rows=5)
    file_category = fields.ForeignKey(FileCategory, on_delete=models.SET_NULL, null=True, verbose_name='文件类型')
    grade = fields.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, verbose_name='级别')
    work_unit = fields.ForeignKey(WorkUnit, on_delete=models.SET_NULL, null=True, verbose_name='所在单位')
    topic_category = fields.ForeignKey(TopicCategory, on_delete=models.SET_NULL, null=True, verbose_name='类别主题')
    visits = models.IntegerField('访问次数', default=0)
    downloads = models.IntegerField('下载次数', default=0)
    release_date = fields.DateField(verbose_name='发生时间', options=options1)
    upload_date = models.DateField('上传日期', auto_now_add=True)
    comment_scoring = models.DecimalField('评分', default=5.0, decimal_places=1, max_digits=2)

    class Meta:
        verbose_name = '文件上传'
        verbose_name_plural = verbose_name
        ordering = ('-upload_date', '-comment_scoring', '-id',)

    def __str__(self):
        return self.label

    def clean(self):
        if self.file_category:
            if self.file_category.form == 1:
                if not self.url:
                    raise ValidationError({
                        'url': '文件类型的展现形式为超链接，本字段必填'
                    })
            else:
                if not self.file:
                    raise ValidationError({
                        'file': '请选择需要上传的文件'
                    })
                try:
                    sl = self.SuffixList[self.file_category.form]
                    suffix = self.file.name.split('.')[-1].lower()
                    if suffix not in sl:
                        raise ValidationError({
                            'file': '文件类型的格式只能是 {}'.format(', '.join(sl))
                        })
                    if self.file.size > 31457280:
                        raise ValidationError({
                            'file': '文件大小不超过30MB'
                        })
                except NotImplementedError:
                    pass

    def get_absolute_url(self):
        return "/%i/" % self.id


class Comment(models.Model):
    Scoring = [
        (1, '一分'),
        (2, '两分'),
        (3, '三分'),
        (4, '四分'),
        (5, '五分')]

    label = fields.CharField(verbose_name='评论', max_length=200, blank=True, null=True)
    nickname = fields.CharField(verbose_name='姓名', max_length=200)
    is_audit = fields.SwitchField(verbose_name='是否审核', default=False)
    comment_date = fields.DateTimeField(verbose_name='评论日期', auto_now_add=True)
    scoring = fields.IntegerField(verbose_name='评分', default=5, choices=Scoring)
    file_upload = fields.ForeignKey(FileUpload, on_delete=models.CASCADE, verbose_name='文件名')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ('-comment_date', )

    def __str__(self):
        return '<{}>的评论'.format(self.file_upload.label)


@receiver(post_save, sender=Comment)
def post_save_comment(instance, **kwargs):
    avg_comment_scoring = Comment.objects.filter(file_upload=instance.file_upload).aggregate(avg_scoring=Avg('scoring'))
    instance.file_upload.comment_scoring = avg_comment_scoring['avg_scoring']
    instance.file_upload.save()
