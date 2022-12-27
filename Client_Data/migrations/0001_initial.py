# Generated by Django 4.1.3 on 2022-12-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientTable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('details', models.TextField()),
                ('Client_Previous_Payout', models.SmallIntegerField()),
                ('Production_Suggested_Project_Advance', models.SmallIntegerField()),
                ('Latest_Project_Advance', models.SmallIntegerField()),
                ('Latest_Client_Payout_Status', models.CharField(choices=[('In-Progress', 'In-Progress'), ('Done', 'Done')], default=1, max_length=100)),
                ('Total_Client_Payout', models.SmallIntegerField()),
                ('Contract_Document_Signing_Status', models.CharField(choices=[('SM', 'SM'), ('FM', 'FM')], default=1, max_length=100)),
            ],
        ),
    ]