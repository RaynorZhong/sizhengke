# Generated by Django 3.2.6 on 2021-11-09 15:56

from django.db import migrations, models
import django.db.models.deletion
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cqmu', '0013_auto_20210928_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', simplepro.components.fields.CharField(max_length=200, verbose_name='所在单位')),
                ('seq', simplepro.components.fields.IntegerField(default=0, verbose_name='排序序号')),
            ],
            options={
                'verbose_name': '所在单位',
                'verbose_name_plural': '所在单位',
                'ordering': ('seq',),
            },
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='author',
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='data_source',
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='recommended_tag',
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='description',
            field=simplepro.components.fields.CharField(max_length=200, verbose_name='事件描述'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='presenter',
            field=simplepro.components.fields.CharField(max_length=200, verbose_name='人物名字'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='release_date',
            field=simplepro.components.fields.DateField(verbose_name='发生时间'),
        ),
        migrations.AlterField(
            model_name='topiccategory',
            name='parent',
            field=simplepro.components.fields.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cqmu.topiccategory', verbose_name='上级分类'),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='work_unit',
            field=simplepro.components.fields.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cqmu.workunit', verbose_name='所在单位'),
        ),
    ]
