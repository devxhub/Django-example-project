# Generated by Django 3.2.15 on 2023-03-10 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='faqs.language'),
        ),
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('fr', 'French'), ('es', 'Spanish'), ('de', 'German'), ('it', 'Italian'), ('pt', 'Portuguese'), ('ru', 'Russian'), ('zh', 'Chinese'), ('ja', 'Japanese'), ('ko', 'Korean'), ('ar', 'Arabic'), ('hi', 'Hindi'), ('bn', 'Bengali'), ('pa', 'Punjabi'), ('te', 'Telugu'), ('mr', 'Marathi')], max_length=10, null=True, unique=True, verbose_name='Language Code'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('French', 'French'), ('Spanish', 'Spanish'), ('German', 'German'), ('Italian', 'Italian'), ('Portuguese', 'Portuguese'), ('Russian', 'Russian'), ('Chinese', 'Chinese'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Arabic', 'Arabic'), ('Hindi', 'Hindi'), ('Bengali', 'Bengali'), ('Punjabi', 'Punjabi'), ('Telugu', 'Telugu'), ('Marathi', 'Marathi')], max_length=50, null=True, unique=True, verbose_name='Language Name'),
        ),
    ]
