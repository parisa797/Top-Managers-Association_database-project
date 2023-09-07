

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190217_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='manager',
        ),
    ]
