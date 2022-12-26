# Generated by Django 4.1.3 on 2022-12-24 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='client_table',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('details', models.TextField()),
                ('Client_Previous_Payout', models.IntegerField()),
                ('Production_Suggested_Project_Advance', models.IntegerField()),
                ('Latest_Project_Advance', models.IntegerField()),
                ('Latest_Client_Payout_Status', models.CharField(choices=[('In-Progress', 'In-Progress'), ('Done', 'Done')], default=1, max_length=100)),
                ('Total_Client_Payout', models.IntegerField()),
                ('Contract_Document_Signing_Status', models.CharField(choices=[('SM', 'SM'), ('FM', 'FM')], default=1, max_length=100)),
                ('project', models.ForeignKey(default='NONE', on_delete=django.db.models.deletion.DO_NOTHING, to='admin_panel.project_table')),
            ],
        ),
    ]