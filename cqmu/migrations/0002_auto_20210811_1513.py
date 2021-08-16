# Generated by Django 3.2.6 on 2021-08-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cqmu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='data_source',
            field=models.CharField(default='', max_length=200, verbose_name='数据来源'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='评论日期'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_audit',
            field=models.BooleanField(default=False, verbose_name='是否审核'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='label',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='评论'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='nickname',
            field=models.CharField(max_length=200, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='scoring',
            field=models.IntegerField(choices=[(1, '一分'), (2, '两分'), (3, '三分'), (4, '四分'), (5, '五分')], default=1, verbose_name='评分'),
        ),
        migrations.AlterField(
            model_name='filecategory',
            name='label',
            field=models.CharField(max_length=200, verbose_name='文件类型'),
        ),
        migrations.AlterField(
            model_name='filecategory',
            name='seq',
            field=models.IntegerField(default=0, verbose_name='排序序号'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='author',
            field=models.CharField(max_length=200, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='comment_scoring',
            field=models.DecimalField(decimal_places=1, default=1.0, max_digits=2, verbose_name='评分'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='description',
            field=models.CharField(max_length=200, verbose_name='文件描述'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='downloads',
            field=models.IntegerField(default=0, verbose_name='下载次数'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='label',
            field=models.CharField(max_length=200, verbose_name='文件名'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='presenter',
            field=models.CharField(max_length=200, verbose_name='主讲人'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='recommended_tag',
            field=models.CharField(max_length=200, verbose_name='推荐标签'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='release_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发布日期'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='上传日期'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='visits',
            field=models.IntegerField(default=0, verbose_name='访问次数'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='label',
            field=models.CharField(max_length=200, verbose_name='级别'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='seq',
            field=models.IntegerField(default=0, verbose_name='排序序号'),
        ),
        migrations.AlterField(
            model_name='topiccategory',
            name='label',
            field=models.CharField(max_length=200, verbose_name='类别主题'),
        ),
        migrations.AlterField(
            model_name='topiccategory',
            name='seq',
            field=models.IntegerField(default=0, verbose_name='排序序号'),
        ),
    ]
