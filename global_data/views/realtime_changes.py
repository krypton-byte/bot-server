import socketio
from global_data.models import getInfoGrup, Users
from datetime import datetime
sio=socketio.Server(async_mode='eventlet', cors_allowed_origins='*')
import psutil, time, math
@sio.on("update", namespace="/grup")
def GrupUpdate(sid, data):
    nama_grup = data.get("nama_grup")
    chat_id   = data.get("chat_id")
    prefix    = data.get("prefix")
    nsfw      = data.get("nsfw")
    AntiToxic = data.get("AntiToxic")
    from_bot  = data.get("from_bot")
    update=getInfoGrup.objects.filter(chat_id=chat_id)
    if update:
        grup = update[0]
        grup.nama_grup = nama_grup
        grup.prefix    = prefix
        grup.nsfw      = nsfw
        grup.AntiToxic = AntiToxic
        grup.LastUpdate = datetime.now()
        grup.save()
    else:
        getInfoGrup(nama_grup=nama_grup, chat_id=chat_id, prefix=prefix,LastUpdate=datetime.now(), nsfw=nsfw, AntiToxic=AntiToxic).save()
    sio.emit("GrupBot", data={"nama_grup":nama_grup, "chat_id":chat_id, "prefix":prefix, "nsfw":nsfw, "AntiToxic":AntiToxic, "from_bot":from_bot}, broadcast=True, namespace="/bot")
@sio.on("user", namespace="/user")
def UserUpdate(sid, data):
    nama    = data.get("nama")
    umur    = data.get("umur")
    gender  = data.get("gender")
    bio     = data.get("bio")
    profile = data.get("profile")
    chat_id = data.get("chat_id")
    from_bot= data.get("from_bot") #nomer bot asal / sumber bot
    from_id = data.get("from_id") #chat_id agar merespon
    if (update:=Users.objects.filter(chat_id=chat_id)):
        user            = update[0]
        user.nama       = nama
        user.umur       = umur
        user.gender     = gender
        user.bio        = bio
        user.profile    = profile
        user.LastUpdate = datetime.now()
        user.save()
    else:
        Users(nama=nama, umur=umur, gender=gender, bio=bio, profile=profile, chat_id=chat_id, LastUpdate=datetime.now()).save()
    sio.emit("UserBot", data={"nama":nama, "umur":umur, "gender":gender, "bio":bio, "profile":profile, "chat_id":chat_id, "from_bot":from_bot, "from_id":from_id}, broadcast=True, namespace="/bot")


@sio.on("broadcast", namespace="/bc")
def brodcast(sid, data):
    sio.emit("cmd", data=data, namespace="/bot", broadcast=True)

@sio.on("sambung", namespace="/grup")
def reques(sid, data):
    print("tersambung")
    print(data)
    sio.emit("resp", data, broadcast=True, namespace="/x")
    return ""

@sio.on("server_", namespace="/about")
def About(sid, data=None):
    boot=time.time()-psutil.boot_time()
    sio.emit("percent", data={
        "boot_time":{"day":int(math.floor(boot/3600)/24),"hours":math.floor(boot/3600)%24, "minute":int(math.floor(boot/60)%60), "second":math.floor(boot%60)},
        "cpu_percent":f"{int(psutil.cpu_percent())}%",
        "disk_percent":f"{int(psutil.virtual_memory().percent)}%"
    }, room=sid,namespace="/about")