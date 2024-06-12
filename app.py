import newrelic.agent
from flask import Flask, jsonify

# Configuración de New Relic
newrelic.agent.initialize('newrelic.ini')
application = newrelic.agent.register_application(timeout=10)

app = Flask(__name__)

@app.route('/')
@newrelic.agent.background_task(application=application, name='hello-world', group='Task')
def hello_world():
    return "Hola Mundo"

@app.route('/error400')
@newrelic.agent.background_task(application=application, name='error-400', group='Task')
def error_400():
    return jsonify({"error": "Bad Request"}), 400

@app.route('/error500')
@newrelic.agent.background_task(application=application, name='error-500', group='Task')
def error_500():
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
