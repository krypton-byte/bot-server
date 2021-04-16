from django.contrib import admin
from global_data.models import Sticker, getInfoGrup, Users
class StickerSaver(admin.ModelAdmin):
    list_display  = ["pengguna","nama"]
    search_fields = ["pengguna", "nama"]
    list_filter   = ["dibuat"]
    list_per_page = 7
class InfoGrup(admin.ModelAdmin):
    list_display  = ["nama_grup","chat_id"]
    search_field   = ["nama_grup","chat_id"]
    list_filter   = ["LastUpdate"]
    list_per_page = 7
class User(admin.ModelAdmin):
    list_display  = ["nama","gender"]
    search_field  = ["chat_id","nama"]
    list_filter   = ["LastUpdate", "gender","umur"]
    list_per_page = 7
admin.site.register(Sticker,StickerSaver)
admin.site.register(getInfoGrup, InfoGrup)
admin.site.register(Users, User)
# Register your models here.
