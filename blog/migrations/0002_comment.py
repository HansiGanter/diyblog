# Generated by Django 4.2.6 on 2023-11-13 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postdate', models.DateField()),
                ('content', models.TextField(help_text='Add your comment here ...', max_length=500)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='blog.author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='blog.blog')),
            ],
        ),
    ]
