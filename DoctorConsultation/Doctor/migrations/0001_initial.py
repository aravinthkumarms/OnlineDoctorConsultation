# Generated by Django 3.2.9 on 2021-12-10 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClinicName', models.CharField(max_length=100)),
                ('ClinicAddress', models.CharField(max_length=100)),
                ('ClinicCity', models.CharField(max_length=100)),
                ('ClinicPhone', models.CharField(max_length=100)),
                ('ClinicEmail', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DoctorImage', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('DoctorName', models.CharField(max_length=100)),
                ('DoctorEmail', models.EmailField(max_length=100)),
                ('DoctorPhone', models.CharField(max_length=100)),
                ('DoctorCity', models.CharField(max_length=100)),
                ('DoctorSpecialization', models.CharField(max_length=100)),
                ('DoctorAge', models.IntegerField()),
                ('DoctorGender', models.CharField(max_length=100)),
                ('DoctorAvailability1', models.CharField(max_length=100)),
                ('DoctorAvailability2', models.CharField(max_length=100)),
                ('DoctorClinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinic', to='Doctor.clinic')),
            ],
        ),
    ]
