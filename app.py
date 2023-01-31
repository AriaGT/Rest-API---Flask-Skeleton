# Importaciones

from flask import Flask, jsonify
from config import config
from routes.products import productsRouter

# Configuración

app = Flask(__name__)

port = config["api"]["port"]

# Rutas

app.register_blueprint(productsRouter)

# Correr Servidor

@app.route('/api/v1/')
def showStatus():
  return jsonify({
    "Server Port": port,
    "Status": "Ok!"
  })

if __name__ == '__main__':
  app.run(debug = True, port = port)
