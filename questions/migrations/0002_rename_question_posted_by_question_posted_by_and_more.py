# Generated by Django 4.1.7 on 2023-02-17 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="question_posted_by",
            new_name="posted_by",
        ),
        migrations.RenameField(
            model_name="question",
            old_name="pub_date",
            new_name="posted_date",
        ),
        migrations.RenameField(
            model_name="question",
            old_name="question_text",
            new_name="text",
        ),
        migrations.RenameField(
            model_name="question",
            old_name="question_title",
            new_name="title",
        ),
    ]
