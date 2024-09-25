# Generated by Django 5.1.1 on 2024-09-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='title',
            field=models.CharField(choices=[('None', ''), ('Mr.', 'Mister'), ('Ms.', 'Ms.'), ('Mx.', 'Mx.'), ('Mrs.', 'Missus'), ('Miss', 'Miss'), ('Dr.', 'Doctor'), ('Sir', 'Sir'), ('Dame', 'Dame'), ('Lord', 'Lord'), ('Lady', 'Lady')], default=None, max_length=4),
        ),
    ]
