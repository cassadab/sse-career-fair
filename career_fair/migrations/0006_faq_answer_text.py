# Generated by Django 2.2.3 on 2019-08-04 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_fair', '0005_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_text',
            field=models.CharField(default='<answer-text>', max_length=255),
        ),
    ]