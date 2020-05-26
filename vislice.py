import bottle
import model



SKRIVNOST = 'moja skrivnost'
PISKOTEK = 'idigre'
DATOTEKA = 'stanje.json'

vislice = model.Vislice('stanje.json')

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/nova-igra/')
def nova_igra():
    id_nove_igre = vislice.nova_igra()
    bottle.response.set_cookie(PISKOTEK, str(id_igre), path='/', secret=SKRIVNOST)
    bottle.redirect("/igra/")

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    igra, poskus = vislice.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, poskus=poskus, id_igre=id_igre)

@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre,crka)
    bottle.redirect('/igra/')


@bottle.get('/img/<slika>')
def pokazi_sliko(slika):
    return bottle.static_file(slika, root='img')

# reloader true da nerabmo na novo skos poganjat
#debuger true da nam pokaže napake
bottle.run(reloader=True, debug=True)