# Generated by Django 3.2.6 on 2023-11-13 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_quality', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Profile', editable=False, max_length=50)),
                ('Height', models.IntegerField()),
                ('Weight', models.IntegerField()),
                ('RecipeWebUsage', models.CharField(choices=[(None, ''), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], default=None, max_length=300, verbose_name='RecipeWebUsage')),
                ('HomeCook', models.CharField(choices=[(None, ''), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], default=None, max_length=300, verbose_name='HomeCook')),
                ('CookingExp', models.CharField(choices=[(None, ''), ('Very_Low', 'Very Low'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Very_High', 'Very High')], default=None, max_length=300, verbose_name='CookingExp')),
                ('EatingGoals', models.CharField(choices=[(None, ''), ('Lose Weight', 'Lose Weight'), ('Gain Weight', 'Gain Weigh'), ('No Goal', 'No Goal')], default=None, max_length=300, verbose_name='HomeCook')),
                ('Depression', models.CharField(choices=[(None, ''), ('Not at all', 'Not at all'), ('Somewhat', 'Somewhat'), ('Quite a lot', 'Quite a lot')], default=None, max_length=300, verbose_name='mood')),
                ('PhysicalActivity', models.CharField(choices=[(None, ''), ('A lot (>9h)', 'A lot >9h'), ('Average (=6h)', 'Average (=6h)'), ('Not enough (<3h)', 'Not enough (<3h)')], default=None, max_length=300, verbose_name='PhysicalActivity')),
                ('SleepHours', models.CharField(choices=[(None, ''), ('≤7h', '≤7h'), ('7-9h', '7-9h'), ('≥9h', '≥9h')], default=None, max_length=300, verbose_name='sleephours')),
                ('CookingTime', models.CharField(choices=[(None, ''), ('≤30min', '≤30min'), ('30-60min', '30-60min'), ('≥60min', '≥60min')], default=None, max_length=300, verbose_name='CookingTime')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_quality.personal_info')),
            ],
            options={
                'verbose_name': 'Profile',
                'db_table': 'Profile',
                'ordering': ['id'],
            },
        ),
    ]