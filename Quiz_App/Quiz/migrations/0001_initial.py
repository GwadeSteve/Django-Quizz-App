# Generated by Django 4.0.4 on 2023-10-12 14:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('op1', models.CharField(max_length=150)),
                ('op2', models.CharField(max_length=150)),
                ('op3', models.CharField(max_length=150)),
                ('op4', models.CharField(max_length=150)),
                ('answer', models.CharField(choices=[('op1', 'Option 1'), ('op2', 'Option 2'), ('op3', 'Option 3'), ('op4', 'Option 4')], max_length=3)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
    ]
