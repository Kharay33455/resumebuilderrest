# Generated by Django 5.2 on 2025-05-03 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_candidate_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='picture',
            field=models.ImageField(default=1, upload_to='pfp'),
            preserve_default=False,
        ),
    ]
