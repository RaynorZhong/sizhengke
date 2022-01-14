# Generated by Django 3.2.6 on 2022-01-14 15:40

from django.db import migrations, models
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cqmu', '0015_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_size', models.URLField(verbose_name='首页图片')),
                ('seq', simplepro.components.fields.IntegerField(default=0, verbose_name='排序序号')),
            ],
            options={
                'verbose_name': '首页图片',
                'verbose_name_plural': '首页图片',
                'ordering': ('seq',),
            },
        ),
        migrations.AlterModelOptions(
            name='fileupload',
            options={'ordering': ('-upload_date', '-id'), 'verbose_name': '文件上传', 'verbose_name_plural': '文件上传'},
        ),
    ]