import bottle

import model

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/igra/')
def nova_igra():
    id_nove_igre = vislice.nova_igra()
    bottle.redirect(f"/igra/{id_nove_igre}/")

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, poskus = vislice.igre[id_igre]

    return bottle.template('igra.tpl', igra=igra, poskus=poskus, id_igre=id_igre)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode('crka')

    vislice.ugibaj(id_igre,crka)

    bottle.redirect(f'/igra/{id_igre}/')



# reloader true da nerabmo na novo skos poganjat
#debuger true da nam pokaže napake
bottle.run(reloader=True, debug=True)