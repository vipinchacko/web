# Generated by Django 2.0.1 on 2018-02-01 21:39

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_useraction'),
    ]

    operations = [
        migrations.CreateModel(
            name='BountyFulfillment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('fulfiller_address', models.CharField(max_length=50)),
                ('fulfiller_email', models.CharField(blank=True, max_length=255)),
                ('fulfiller_github_username', models.CharField(blank=True, max_length=255)),
                ('fulfiller_name', models.CharField(blank=True, max_length=255)),
                ('fulfiller_metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={})),
                ('fulfillment_id', models.IntegerField(blank=True, null=True)),
                ('accepted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bounty',
            name='submissions_comment',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bountyfulfillment',
            name='bounty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fulfillments', to='dashboard.Bounty'),
        ),
        migrations.AddField(
            model_name='bountyfulfillment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fulfilled', to='dashboard.Profile', null=True),
        ),
    ]
