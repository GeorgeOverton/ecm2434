# Generated by Django 4.1.7 on 2023-03-21 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_alter_user_profile_background_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_background',
            field=models.ForeignKey(default=None, null=True, on_delete=models.SET(71), related_name='profile_background', to='database.shopitem'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_border',
            field=models.ForeignKey(default=None, null=True, on_delete=models.SET(72), related_name='profile_border', to='database.shopitem'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ForeignKey(default=None, null=True, on_delete=models.SET(49), related_name='profile_pic', to='database.shopitem'),
        ),
    ]