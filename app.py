
from flask import Flask, jsonify, request, session
from flask_cors import CORS


from user import User
from userDB import add_user, select_all
from emitefactura import Factura, BunuriServicii
from emiteFacturaDB import add_factura, add_bunuri, get_facturi
from delegat import Delegat
from delegatDB import get_delegati ,add_delegat, sterge_delegat, update_delegat
from emitent import Emitent
from emitentDB import get_emitent, update_emitent
from client import Client
from clientDB import get_clienti, get_one_client, add_client, delete_client, update_client
from oFactura import numar_factura, get_one_client_after_id, get_one_delegat_after_id, get_bunuri_after_fact_number

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = 'nadgob19811981'

@app.route('/')
def home():
    return jsonify('merge si asa')

#******************************************************
# creaza user routes
#******************************************************

@app.route('/user/contNou', methods=['POST'])
def creaza_cont():
    user_date = request.json
    print(user_date)
    utilizatori = select_all()
    print(utilizatori)
    for i in utilizatori:
        if user_date['userName'] == i[0] or user_date['email'] == i[1]:
            return jsonify('Utilizatorul exista')
    newUser = User( user_date['userName'], user_date['email'], user_date['functia'], user_date['password'] )
    add_user(newUser)
    return jsonify('Sa creat cont nou')

@app.route('/login', methods=['POST'])
def login_function():
    login_date = request.json
    utilizatori = select_all()
    for i in utilizatori:
        if login_date['userName'] == i[0] or login_date['userName'] == i[1]:
            if login_date['password'] == i[3]:
                session['loggedIn'] = True
                print( 'merge login', session['loggedIn'] )
                return jsonify('Esti logat')
    
    return jsonify('Nu esti logat')

@app.route('/state')
def get_state():
    print('merge state - ', session['loggedIn'])
    if 'loggedIn' in session:
        print('da este in session')
        return jsonify('da este')
    return jsonify('nu este in session')

@app.route('/logout')
def logout_function():
    print('merge logout - ')
    if 'loggedIn' in session:
        session.pop('loggedIn')
        print( 'este pop out ')
    return jsonify('false')

#******************************************************
# emite factura routes
#******************************************************

@app.route('/facturaSingura')
def get_o_factura():
    f = request.args.get('nr')
    print(f)
    factura = numar_factura(f)
    client = get_one_client_after_id(factura[3])
    delegat = get_one_delegat_after_id(factura[4])
    bunuri = get_bunuri_after_fact_number(factura[1])
    print(factura, client, delegat, bunuri)
    return jsonify(factura, client, delegat, bunuri)

@app.route('/factura')
def get_factura():
    response = get_facturi()
    log = True
    print(response)
    return jsonify(response, log)

@app.route('/factura/add', methods=['POST'])
def factura_add():
    res = request.json
    bunuri = res['date']['bunuriServicii']
    fact = Factura(res['date']['serieFactura'], res['date']['numarFactura'], res['date']['dataFactura'], res['clientId'], res['delegatId'])
    add_factura(fact)
    for i in range( 0, len(res['date']['bunuriServicii']) ):
        print(i)
        bs = BunuriServicii(bunuri[i]['denumire'], bunuri[i]['cantitate'],  bunuri[i]['fel'], bunuri[i]['pretBucata'], bunuri[i]['cotaTva'], res['date']['numarFactura'])
        add_bunuri(bs)
    return jsonify('a mers')


#******************************************************
# clients routes
#******************************************************

@app.route('/clients')
def clients():
    nume = request.args.get('nume')
    if (nume == None):
        clienti = get_clienti()
        if(clienti == None):
            return jsonify('nu ai clienti')
        else:
            return jsonify(clienti)
    else:
        print('argumentul este', nume)
        cl = get_one_client(nume)
        return jsonify(cl)

    
@app.route('/client/add', methods=['POST'])
def clients_add():
    res = request.json
    cl = Client(res['numeClient'], res['tipClient'], res['regCom'], res['codFiscal'], res['codTva'], res['telefon'], res['email'])
    add_client(cl)
    return jsonify('gata si cu clientul')

@app.route('/client/delete', methods=['DELETE'])
def clients_delete():
    id = request.json['i']
    delete_client(id)
    return jsonify('clientul a fost sters')

@app.route('/client/update', methods=['PUT'])
def clients_update():
    cl = request.json
    print(cl)
    update_client(cl)
    return jsonify('clientul a fost updatat.')



#******************************************************
# emitent routes
#******************************************************

@app.route('/emitent')
def emitent():
    emi = get_emitent()
    return jsonify(emi)

@app.route('/emitent/update', methods=['PUT'])
def emitent_update():
    res = request.json
    emi = Emitent(
        res['numeSocietate'],
        res['tipSocietate'],
        res['regComertului'],
        res['codFiscal'],
        res['codTva'],
        res['capitalSocial'],
        res['localitate'],
        res['strada'],
        res['numar'],
        res['scara'],
        res['apartament'],
        res['judet'],
        res['telefon'],
        res['email'],
        res['contIBAN'],
        res['denumireBanca'],
    )
    update_emitent(emi)
    return jsonify('Datele au fost salvate.')

#******************************************************
# delegat routes
#******************************************************


@app.route('/delegat')
def delegat_get():
    rezultat = get_delegati()
    if rezultat == []:
        return jsonify('nu exista delegati')
    return jsonify(rezultat)


@app.route('/delegat/add', methods=['POST'])
def delegat_add():
    res = request.json
    d = Delegat(res['nume'], res['prenume'], res['buletin'], res['masina'])
    add_delegat(d)
    return jsonify(res)

@app.route('/delegat/sterge', methods=['DELETE'])
def delegat_sterge():
    id = request.json['i']
    sterge_delegat(id)
    return jsonify('a mers')

@app.route('/delegat/update', methods=['PUT'])
def delegat_update():
    date = request.json
    d = Delegat(date['nume'], date['prenume'], date['buletin'], date['masina'])
    i = date['id']
    update_delegat(d, i)
    return jsonify('a mers si updateul')


if __name__ == '__main__':
    app.run()