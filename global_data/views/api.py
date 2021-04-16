from global_data.views.realtime_changes import reques
from django.shortcuts import render
from global_data.models import Sticker, Users, getInfoGrup
from django.http import JsonResponse
import datetime
def AllInfoGrup(request):
    return JsonResponse({"result":list(map(lambda obj:{"nama_grup":obj.nama_grup, "chat_id":obj.chat_id, "prefix":obj.prefix, "nsfw":obj.nsfw, "AntiToxic":obj.AntiToxic}, getInfoGrup.objects.all()))})
def allUser(request):
    return JsonResponse({
        "result":list(map(lambda obj:{"nama":obj.nama,"umur":obj.umur, "gender":obj.gender,"bio":obj.bio,"profile":obj.profile, "chat_id":obj.chat_id}, Users.objects.all()))
    })
def index(request):
    return render(request, "index.html", {})
def uploadSticker(request):
    if request.GET.get("pengguna") and request.GET.get("nama") and request.GET.get("konten"):
        if Sticker.objects.filter(nama=request.GET.get("nama"), pengguna=request.GET.get("pengguna")):
            return JsonResponse({
                "status":False,
                "sticker":f"{request.GET.get('nama')}",
                "tersimpan":True
            })
        else:
            Sticker(nama=request.GET.get("nama"),pengguna=request.GET.get("pengguna"), dibuat=datetime.datetime.now(), konten=request.GET.get("konten")).save()
            return JsonResponse({
                "status":True,
                "sticker":f"{request.GET.get('nama')}",
                "tersimpan":True
            })
    else:
        return JsonResponse({
            "status":False
        })
def Index(request):
    return JsonResponse({})
def DeleteSticker(request):
    if request.GET.get("pengguna") and request.GET.get("nama"):
        if Sticker.objects.filter(pengguna=request.GET.get("pengguna"), nama=request.GET.get("nama")).delete()[0] > 0:
            return JsonResponse({
                "status":True,
                "sticker":f"{request.GET.get('nama')}",
                "terhapus":True
            })
        else:
            return JsonResponse({
                "status":False,
                "sticker":f"{request.GET.get('nama')}",
                "terhapus":False
        })
    else:
        return JsonResponse({})
def getSticker(request):
    saved=Sticker.objects.filter(pengguna=request.GET.get("pengguna"), nama=request.GET.get("nama"))
    if saved:
        return JsonResponse({
            "status":True,
            "nama":saved[0].nama,
            "konten":saved[0].konten,
            "tersimpan":True
        })
    else:
        return JsonResponse({
            "status":False,
            "nama":request.GET.get("nama"),
            "kontent":None,
            "tersimpan":False
        })
def getListSticker(request):
    return JsonResponse({
        "pengguna":request.GET.get("pengguna"),
        "sticker":list(map(lambda x:x.nama, Sticker.objects.filter(pengguna=request.GET.get("pengguna"))))
        })


# Create your views here.
