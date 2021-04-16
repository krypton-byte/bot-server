from typing import BinaryIO
from django.db import models
class Sticker(models.Model):
    nama     = models.CharField(max_length=100)
    pengguna = models.CharField(max_length=30)
    dibuat   = models.DateTimeField()
    konten  = models.CharField(max_length=50) 
    def __str__(self):
        return self.nama

class getInfoGrup(models.Model):
    nama_grup  = models.TextField()
    chat_id    = models.CharField(max_length=60)
    prefix     = models.TextField()
    nsfw       = models.IntegerField()
    AntiToxic  = models.IntegerField()
    LastUpdate = models.DateTimeField()
    def __str__(self):
        return self.nama_grup
class Users(models.Model):
    nama       = models.TextField()
    umur       = models.IntegerField()
    gender     = models.TextField()
    bio        = models.TextField()
    profile    = models.TextField()
    chat_id    = models.TextField()
    bot_save   = models.TextField()
    LastUpdate = models.DateTimeField()
    def __str__(self):
        return self.nama
# Create your models here.
