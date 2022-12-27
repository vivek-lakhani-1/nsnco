# Generated by Django 4.1.3 on 2022-12-27 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Artist', '__first__'),
        ('Client_Data', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Project_Table',
            fields=[
                ('project', models.IntegerField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('post_project_client_feedbacks', models.TextField()),
                ('project_fees_status', models.CharField(choices=[('Unpaid', 'Unpaid'), ('Partially', 'Partially'), ('Paid', 'Paid')], default=1, max_length=10)),
                ('Contract_Document_Signing_Status', models.CharField(choices=[('SM', 'SM'), ('FM', 'FM')], default=1, max_length=10)),
                ('assigned_artist', models.ManyToManyField(related_name='ArtistTable4', to='Artist.artisttable')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ClientTable5', to='Client_Data.clienttable')),
                ('project_demo', models.ManyToManyField(related_name='ProjectDemos2', to='Artist.projectdemos')),
                ('shorlisted_artist', models.ManyToManyField(related_name='ArtistTable5', to='Artist.artisttable')),
                ('showcase_demo', models.ManyToManyField(related_name='worklink1', to='Artist.worklink')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution_fee', models.SmallIntegerField()),
                ('Production_Advance', models.SmallIntegerField()),
                ('Negotiated_Advance', models.SmallIntegerField()),
                ('Final_Advance', models.SmallIntegerField()),
                ('Advance_Status', models.CharField(choices=[('In-Progress', 'In-Progress'), ('Done', 'Done')], default=1, max_length=100)),
                ('Assigned_Artists_Payouts', models.CharField(max_length=100)),
                ('Assigned_Artists_Advance_Payout_Status', models.CharField(choices=[('In-Progress', 'In-Progress'), ('Done', 'Done')], default=1, max_length=100)),
                ('Final_Fee_Settlement_Status', models.BooleanField()),
                ('Post_Project_Client_Total_Payout', models.SmallIntegerField()),
                ('project_fee_status', models.CharField(choices=[('SM', 'SM'), ('FM', 'FM')], default=1, max_length=100)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ClientTable3', to='Client_Data.clienttable')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Project_Table0', to='Artist_Project.project_table')),
            ],
        ),
    ]
