import newrelic.agent
from flask import Flask, jsonify, abort

# Configuración de New Relic
newrelic.agent.initialize('newrelic.ini')
application = newrelic.agent.register_application(timeout=10)

app = Flask(__name__)

@app.route('/')
@newrelic.agent.background_task(application=application, name='hello-world', group='Task')
def hello_world():
    return "Hola Mundo"

@app.route('/error400')
@newrelic.agent.background_task(application=application, name='error-400', group='Error')
def error_400():
    abort(400)

@app.route('/error500')
@newrelic.agent.background_task(application=application, name='error-500', group='Error')
def error_500():
    abort(500)

@app.errorhandler(400)
def handle_400_error(e):
    return jsonify(error=str(e)), 400

@app.errorhandler(500)
def handle_500_error(e):
    return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
