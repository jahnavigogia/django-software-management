
# Generated by Django 5.0.3 on 2024-04-23 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0004_alter_document_id_alter_software_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='license',
            field=models.IntegerField(serialize=False),
        ),
    ]