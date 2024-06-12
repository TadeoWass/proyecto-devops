import newrelic.agent
from flask import Flask

# Configuración de New Relic
newrelic.agent.initialize('newrelic.ini')
application = newrelic.agent.register_application(timeout=10)

app = Flask(__name__)

@app.route('/')
@newrelic.agent.background_task(application=application, name='hello-world', group='Task')
def hello_world():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)