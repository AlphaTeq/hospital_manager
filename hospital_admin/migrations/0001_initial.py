# Generated by Django 4.2.5 on 2025-06-03 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_Information',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('test_name', models.CharField(blank=True, max_length=200, null=True)),
                ('test_price', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='specialization',
            fields=[
                ('specialization_id', models.AutoField(primary_key=True, serialize=False)),
                ('specialization_name', models.CharField(blank=True, max_length=200, null=True)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital_information')),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(blank=True, max_length=200, null=True)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital_information')),
            ],
        ),
        migrations.CreateModel(
            name='hospital_department',
            fields=[
                ('hospital_department_id', models.AutoField(primary_key=True, serialize=False)),
                ('hospital_department_name', models.CharField(blank=True, max_length=200, null=True)),
                ('featured_image', models.ImageField(blank=True, default='departments/default.png', null=True, upload_to='departments/')),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital_information')),
            ],
        ),
        migrations.CreateModel(
            name='Clinical_Laboratory_Technician',
            fields=[
                ('technician_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('featured_image', models.ImageField(blank=True, default='technician/user-default.png', null=True, upload_to='technician/')),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.hospital_information')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='technician', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Admin_Information',
            fields=[
                ('admin_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('featured_image', models.ImageField(blank=True, default='admin/user-default.png', null=True, upload_to='admin/')),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('role', models.CharField(blank=True, choices=[('hospital', 'hospital'), ('laboratory', 'laboratory'), ('pharmacy', 'pharmacy')], max_length=200, null=True)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.hospital_information')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hospital_admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
