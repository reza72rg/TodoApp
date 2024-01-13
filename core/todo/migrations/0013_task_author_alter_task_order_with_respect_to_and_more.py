# Generated by Django 4.2.2 on 2023-12-23 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
        ("todo", "0012_alter_task_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="posts_author",
                to="accounts.profile",
            ),
        ),
        migrations.AlterOrderWithRespectTo(
            name="task",
            order_with_respect_to="author",
        ),
        migrations.RemoveField(
            model_name="task",
            name="user",
        ),
    ]
