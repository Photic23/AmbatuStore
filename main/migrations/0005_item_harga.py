# Generated by Django 4.2.5 on 2023-10-04 00:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_alter_item_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="harga",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]