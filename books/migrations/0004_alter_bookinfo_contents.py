# Generated by Django 3.2.5 on 2021-09-28 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_bookinfo_contents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='contents',
            field=models.TextField(),
        ),
    ]
