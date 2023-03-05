# Generated by Django 4.1.7 on 2023-03-04 22:59

from django.db import migrations, models
import djangojokes.storage_backends
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_applicant_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.FileField(blank=True, help_text='PDFs only', storage=djangojokes.storage_backends.PrivateMediaStorage(), upload_to='resumes', validators=[jobs.models.validate_pdf]),
        ),
    ]