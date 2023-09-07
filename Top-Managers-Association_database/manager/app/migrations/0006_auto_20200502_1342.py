

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_contact_manager'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={},
        ),
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.CharField(
                choices=[('male', 'Male'), ('female', 'Female')], max_length=50),
        ),
    ]
