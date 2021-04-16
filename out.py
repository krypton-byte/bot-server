__all__ = ['out']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['stickerPackID', 'fs_1', 'createExif', 'googleLink', 'appleLink'])
@Js
def PyJsHoisted_createExif_(packname, author, this, arguments, var=var):
    var = Scope({'packname':packname, 'author':author, 'this':this, 'arguments':arguments}, var)
    var.registers(['f', 'ffff', 'json', 'fff', 'packname', 'length', 'author', 'code', 'ff', 'buffer'])
    var.put('json', Js({'sticker-pack-id':var.get('stickerPackID'),'sticker-pack-name':var.get('packname'),'sticker-pack-publisher':var.get('author'),'android-app-store-link':var.get('googlelink'),'ios-app-store-link':var.get('applelink')}))
    var.put('length', var.get('JSON').callprop('stringify', var.get('json')).get('length'))
    var.put('f', var.get('Buffer').callprop('from', Js([Js(73), Js(73), Js(42), Js(0), Js(8), Js(0), Js(0), Js(0), Js(1), Js(0), Js(65), Js(87), Js(7), Js(0)])))
    var.put('code', Js([Js(0), Js(0), Js(22), Js(0), Js(0), Js(0)]))
    if (var.get('length')>Js(256.0)):
        var.put('length', (var.get('length')-Js(256.0)))
        var.get('code').callprop('unshift', Js(1))
    else:
        var.get('code').callprop('unshift', Js(0))
    var.put('fff', var.get('Buffer').callprop('from', var.get('code')))
    var.put('ffff', var.get('Buffer').callprop('from', var.get('JSON').callprop('stringify', var.get('json'))))
    if (var.get('length')<Js(16.0)):
        var.put('length', var.get('length').callprop('toString', Js(16.0)))
        var.put('length', (Js('0')+var.get('length')))
    else:
        var.put('length', var.get('length').callprop('toString', Js(16.0)))
    var.put('ff', var.get('Buffer').callprop('from', var.get('length'), Js('hex')))
    var.put('buffer', var.get('Buffer').callprop('concat', Js([var.get('f'), var.get('ff'), var.get('fff'), var.get('ffff')])))
    @Js
    def PyJs_anonymous_0_(err, this, arguments, var=var):
        var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
        var.registers(['err'])
        if var.get('err'):
            return var.get('console').callprop('error', var.get('err'))
    PyJs_anonymous_0_._set_name('anonymous')
    var.get('fs_1').callprop('writeFile', Js('data.exif'), var.get('buffer'), PyJs_anonymous_0_)
PyJsHoisted_createExif_.func_name = 'createExif'
var.put('createExif', PyJsHoisted_createExif_)
Js('use strict')
var.put('fs_1', var.get('require')(Js('fs')))
var.put('stickerPackID', Js('com.snowcorp.stickerly.android.stickercontentprovider b5e7275f-f1de-4137-961f-57becfad34f2'))
var.put('googleLink', Js('https://play.google.com/store/apps/details?id=com.marsconstd.stickermakerforwhatsapp'))
var.put('appleLink', Js('https://itunes.apple.com/app/sticker-maker-studio/id1443326857'))
pass
pass


# Add lib to the module scope
out = var.to_python()