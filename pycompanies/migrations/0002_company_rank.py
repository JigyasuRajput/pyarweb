from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pycompanies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='rank',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
