# Generated by Django 3.2.6 on 2021-08-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cqmu', '0006_auto_20210813_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filecategory',
            name='form',
            field=models.IntegerField(choices=[(1, '超链接'), (2, '文件-下载按钮'), (3, '图片-下载按钮'), (4, '音频-下载按钮'), (5, '视频-下载按钮')], default=1, verbose_name='展现形式'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='comment_scoring',
            field=models.DecimalField(decimal_places=1, default=5.0, max_digits=2, verbose_name='评分'),
        ),
    ]
