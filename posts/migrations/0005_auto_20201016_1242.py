# Generated by Django 3.1.2 on 2020-10-16 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_post_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pric',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='post',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]