# Generated by Django 4.1.3 on 2022-12-29 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Artist_Project', '0001_initial'),
        ('Artist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdemos',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Project_Table3', to='Artist_Project.project_table'),
        ),
    ]
