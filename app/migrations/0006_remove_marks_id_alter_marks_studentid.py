# Generated by Django 4.0.4 on 2022-05-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_computermarks_marks_languagemakrs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='id',
        ),
        migrations.AlterField(
            model_name='marks',
            name='StudentId',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
