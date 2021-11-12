# Generated by Django 3.2.6 on 2021-11-12 11:05

from django.db import migrations, models
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cqmu', '0014_auto_20211109_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_size', models.URLField(verbose_name='主题图片-大尺寸')),
                ('small_size', models.URLField(verbose_name='主题图片-小尺寸')),
                ('seq', simplepro.components.fields.IntegerField(default=0, verbose_name='排序序号')),
            ],
            options={
                'verbose_name': '主题图片',
                'verbose_name_plural': '主题图片',
                'ordering': ('seq',),
            },
        ),
    ]