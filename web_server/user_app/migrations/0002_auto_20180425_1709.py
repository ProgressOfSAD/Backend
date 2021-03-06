# Generated by Django 2.0.3 on 2018-04-25 09:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activerecord',
            name='active',
            field=models.IntegerField(choices=[(0, '预约'), (1, '借阅')], default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activerecord',
            name='active_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activerecord',
            name='bid',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='user_app.BookInstance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activerecord',
            name='uid',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='user_app.UserInfo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='state',
            field=models.IntegerField(choices=[(0, '正常'), (1, '被预约'), (2, '被借出')]),
        ),
    ]
