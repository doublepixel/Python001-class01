# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    p_id = models.CharField(max_length=255)
    p_name = models.CharField(max_length=255)
    c_id = models.CharField(unique=True, max_length=255)
    n_star = models.IntegerField()
    short = models.CharField(max_length=400)
    c_time = models.CharField(max_length=255)
    sentiment = models.FloatField()
    add_time = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'comment'

class Product(models.Model):
    p_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    p_name = models.CharField(max_length=255, blank=True, null=True)
    p_type = models.CharField(max_length=255, blank=True, null=True)
    add_time = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'product'
