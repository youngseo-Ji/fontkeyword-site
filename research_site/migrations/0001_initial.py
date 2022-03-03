# Generated by Django 3.1.3 on 2022-03-03 07:17

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('name', 'age', 'grade', 'phone')},
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('font_answer', jsonfield.fields.JSONField(default=dict)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research_site.user')),
            ],
        ),
    ]