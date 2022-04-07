from flask import Flask
from products import products

#Objeto que vamos a configurar
app = Flask(__name__)

#Cada vez que un usuario entre a la ruta principal se le va a responder algo
@app.route('/')
def hello_world():
    return 'Hello, Sebastián!'

#rutas    
@app.route('/add_contact')
def add_contact():
    return 'add contact'

@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete')
def delete_contact():
    return 'delete contact'


#Validacion del archivo principal
if __name__ == '__main__':
    app.run(debug=True) #Cada vez que hago cambios se reinicie automaticamente