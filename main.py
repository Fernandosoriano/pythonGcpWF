from flask import Flask
app = Flask(__name__)
from google.cloud.workflows.executions_v1beta.services.executions import ExecutionsClient
from google.cloud.workflows.executions_v1beta.types import CreateExecutionRequest, Execution
import json

# print(':::::::Hola')

@app.route('/inicio')

def callWorkflow():
    project = "My First Project"  
    location = "us-central1"
    workflow = "workflow-prueba-local-2"
    arguments = {"firstName": "Fernando","lastName": "Valle"}

    parent = "projects/{}/locations/{}/workflows/{}".format(project, location, workflow)
    execution = Execution(argument = json.dumps(arguments))

    client = ExecutionsClient()
    response = None
    # Try running a workflow:
    print(':::::::: try run the wf')
    try:
        print(':::::::: try run the wf')

        response = client.create_execution(parent=parent, execution=execution)
    except:
        print(':::::::: except run the wf')
        return ("Error occurred when triggering workflow execution", 500)

    print ("OK", 200)



if __name__ == '__main__':
    app.run(debug=True,port = 4000)

