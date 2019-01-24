# Generated by Django 2.1.5 on 2019-01-23 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editordb', '0004_auto_20190122_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Hours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Minutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='crontab',
            name='days',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editordb.Days'),
        ),
        migrations.AlterField(
            model_name='crontab',
            name='hours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editordb.Hours'),
        ),
        migrations.AlterField(
            model_name='crontab',
            name='minutes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editordb.Minutes'),
        ),
        migrations.DeleteModel(
            name='InfoCrontab',
        ),
    ]
