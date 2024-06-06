import newrelic.agent
from flask import Flask

# Configuración de New Relic
newrelic.agent.initialize('proyecto-devops/newrelic.ini')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hola Mundo"

if __name__ == "__main__":
    # Iniciar la aplicación con New Relic
    newrelic.agent.start_application()
    app.run(host='0.0.0.0', port=5000)
