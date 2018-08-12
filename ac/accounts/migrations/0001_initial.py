# Generated by Django 2.1 on 2018-08-10 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(choices=[('STD', 'base employee'), ('MGR', 'manager'), ('SRMGR', 'senior manager'), ('PRES', 'president')], max_length=25)),
                ('gender', models.CharField(max_length=50)),
                ('job_description', models.TextField()),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('profile_picture', models.FileField(blank=True, upload_to='profileImages')),
                ('salary', models.DecimalField(decimal_places=3, max_digits=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Department')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee', to='accounts.Employee')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]