# Generated by Django 3.2.6 on 2021-08-11 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cqmu', '0002_auto_20210811_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='topic_categroy',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='topic_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cqmu.topiccategory', verbose_name='类别主题'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='file_upload',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cqmu.fileupload', verbose_name='文件上传'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='file_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cqmu.filecategory', verbose_name='文件类型'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cqmu.grade', verbose_name='级别'),
        ),
    ]
