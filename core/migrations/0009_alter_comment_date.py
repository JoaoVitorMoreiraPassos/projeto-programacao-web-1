# Generated by Django 4.2.2 on 2023-07-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_alter_comment_notice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(),
        ),
    ]
