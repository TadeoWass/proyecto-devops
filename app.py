import newrelic.agent
from flask import Flask


# Configuración de New Relic
newrelic.agent.initialize('newrelic.ini')

@newrelic.agent.background_task(name='database-update', group='Task')
def database_update():
    ...

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
