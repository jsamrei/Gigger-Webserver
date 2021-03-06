# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('fb_id', models.BigIntegerField(db_column='FB_ID', db_index=True, unique=True)),
                ('event_id', models.AutoField(db_column='EventID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('cover_source', models.CharField(blank=True, max_length=500)),
                ('start_time', models.CharField(blank=True, max_length=30)),
                ('timezone', models.CharField(blank=True, max_length=45)),
                ('updated_time', models.DateTimeField(blank=True, null=True)),
                ('ticket_uri', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'db_table': 'Event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('meta_description', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.BigAutoField(db_column='LocationID', primary_key=True, serialize=False)),
                ('city', models.CharField(blank=True, db_index=True, max_length=45)),
                ('country', models.CharField(blank=True, db_index=True, max_length=45)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('state', models.CharField(blank=True, db_index=True, max_length=45)),
                ('street', models.CharField(blank=True, max_length=45)),
                ('zip', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'Location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('fb_id', models.BigIntegerField(db_column='FB_ID', db_index=True, unique=True)),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('performer_id', models.AutoField(db_column='PerformerID', primary_key=True, serialize=False)),
                ('about', models.CharField(blank=True, max_length=255)),
                ('bio', models.TextField(blank=True)),
                ('artists_we_like', models.CharField(blank=True, max_length=255)),
                ('band_members', models.CharField(blank=True, max_length=255)),
                ('booking_agent', models.CharField(blank=True, max_length=255)),
                ('category', models.CharField(blank=True, max_length=255)),
                ('cover_id', models.IntegerField(blank=True, null=True)),
                ('cover_source', models.CharField(blank=True, max_length=1000)),
                ('current_location', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('genre', models.CharField(blank=True, max_length=255)),
                ('hometown', models.CharField(blank=True, max_length=255)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('band_type', models.CharField(db_column='BandType', max_length=55)),
                ('record_label', models.CharField(blank=True, max_length=255)),
                ('talking_about_count', models.PositiveIntegerField(null=True)),
                ('website', models.CharField(blank=True, max_length=255)),
                ('twitter_handle', models.CharField(blank=True, db_column='PerformerTwitterHandle', max_length=255)),
                ('sound_path', models.URLField(blank=True, db_column='PerformerSoundCloudPath', max_length=500)),
                ('email_address', models.EmailField(blank=True, db_column='PerformerEmailAddress', max_length=255)),
            ],
            options={
                'db_table': 'Performer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerformerEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'PerformerEvent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('fb_id', models.BigIntegerField(db_column='FB_ID', db_index=True, unique=True)),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('venue_id', models.AutoField(primary_key=True, serialize=False)),
                ('capacity', models.IntegerField(blank=True)),
                ('booking_contact', models.CharField(blank=True, max_length=255)),
                ('about', models.CharField(blank=True, max_length=255)),
                ('category', models.CharField(blank=True, max_length=45)),
                ('checkins', models.IntegerField(null=True)),
                ('cover_id', models.BigIntegerField(null=True)),
                ('cover_source', models.CharField(blank=True, max_length=500)),
                ('description', models.TextField(blank=True)),
                ('likes', models.IntegerField(null=True)),
                ('link', models.CharField(blank=True, max_length=45)),
                ('phone', models.CharField(blank=True, max_length=45)),
                ('talking_about_count', models.IntegerField(null=True)),
                ('were_here_count', models.IntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VenueTechSpec',
            fields=[
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.Venue')),
                ('booking_contact', models.CharField(blank=True, max_length=255)),
                ('production_contact', models.CharField(blank=True, max_length=255)),
                ('venue_hire', models.TextField(blank=True)),
                ('underage_band_members', models.TextField(blank=True)),
                ('technical_info', models.TextField(blank=True)),
                ('room_spec', models.TextField(blank=True)),
                ('pa_spec', models.TextField(blank=True)),
                ('extra_spec', models.TextField(blank=True)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
