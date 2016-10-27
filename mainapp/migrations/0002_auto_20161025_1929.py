# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-25 19:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_gender', models.CharField(max_length=10)),
                ('u_dob', models.DateField(max_length=20)),
                ('u_github', models.CharField(max_length=500)),
                ('u_linkedin', models.CharField(max_length=500)),
                ('u_contact_no', models.CharField(max_length=50)),
                ('u_prof_title', models.CharField(max_length=500)),
                ('u_mentor', models.BooleanField(default=False)),
                ('u_location', models.CharField(max_length=1000)),
                ('u_bio', models.TextField()),
                ('u_current_qualification', models.CharField(max_length=500, null=True)),
                ('u_current_degree', models.CharField(max_length=500)),
                ('u_current_college', models.CharField(max_length=1000)),
                ('u_education_start_year', models.DateField(max_length=20)),
                ('u_education_end_year', models.DateField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor_project', to='mainapp.Student'),
        ),
        migrations.AlterField(
            model_name='project',
            name='p_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_project', to='mainapp.Student'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
