# Generated by Django 4.2.2 on 2023-06-18 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0006_notice_slug_recipedates"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="parent_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="core.comment",
            ),
        ),
    ]