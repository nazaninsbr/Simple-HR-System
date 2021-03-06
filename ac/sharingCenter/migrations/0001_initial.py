# Generated by Django 2.1 on 2018-08-11 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_remove_employee_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('item', models.FileField(blank=True, upload_to='shares')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Employee')),
            ],
        ),
    ]
