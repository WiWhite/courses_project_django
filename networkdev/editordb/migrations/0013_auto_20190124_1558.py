# Generated by Django 2.1.5 on 2019-01-24 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editordb', '0012_auto_20190124_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='days',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='hours',
            name='hours',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='minutes',
            name='minutes',
            field=models.IntegerField(),
        ),
    ]
