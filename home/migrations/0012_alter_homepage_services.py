# Generated by Django 3.2.25 on 2024-06-04 20:20

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_homepage_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='services',
            field=wagtail.fields.StreamField([('service', wagtail.blocks.StructBlock([('icon', wagtail.blocks.CharBlock(required=True)), ('title', wagtail.blocks.CharBlock(required=True)), ('description', wagtail.blocks.TextBlock(required=True))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
