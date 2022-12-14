# Generated by Django 4.0.3 on 2022-09-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_auteur_num_phone_todo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='created_date',
            new_name='date_creation',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='due_date',
            new_name='date_fin',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='titre',
        ),
        migrations.AlterField(
            model_name='auteur',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
