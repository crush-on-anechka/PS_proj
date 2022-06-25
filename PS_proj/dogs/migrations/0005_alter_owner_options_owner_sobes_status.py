# Generated by Django 4.0.5 on 2022-06-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0004_owner_discount_card'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='owner',
            options={'ordering': ['-add_date'], 'verbose_name': 'Хозяин', 'verbose_name_plural': 'Хозяева'},
        ),
        migrations.AddField(
            model_name='owner',
            name='sobes_status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
