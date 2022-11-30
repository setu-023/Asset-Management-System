# Generated by Django 3.2 on 2022-11-29 16:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('device_type', models.CharField(choices=[('mobile', 'mobile'), ('tablet', 'tablet'), ('laptop', 'laptop')], max_length=25)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='DelegateAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('allocated', 'allocated'), ('returned', 'returned')], max_length=25)),
                ('device_condition', models.CharField(choices=[('good', 'good'), ('average', 'average'), ('bad', 'bad')], max_length=25)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.asset')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]
