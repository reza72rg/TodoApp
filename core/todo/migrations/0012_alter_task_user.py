# Generated by Django 4.2.2 on 2023-12-21 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('todo', '0011_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts_author', to='accounts.profile'),
        ),
    ]
