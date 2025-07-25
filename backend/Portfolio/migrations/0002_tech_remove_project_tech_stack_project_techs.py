# Generated by Django 5.2.4 on 2025-07-25 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='tech_icons/')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='tech_stack',
        ),
        migrations.AddField(
            model_name='project',
            name='techs',
            field=models.ManyToManyField(related_name='projects', to='Portfolio.tech'),
        ),
    ]
