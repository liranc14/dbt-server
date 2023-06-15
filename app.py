from flask import Flask, request, Response
from flask_restful import Resource, Api
from shelljob import proc

app = Flask(__name__)
api = Api(app)

# TODO logging to client, unable to get status code

class DbtCommand(Resource):
    def post(self):
        request_data = request.get_json(force=True)
        
        dbt_cmd = f"dbt {request_data['dbt']}"
        
        g = proc.Group()
        g.run([dbt_cmd], shell=True)
        
        def read_process():
            while g.is_pending():
                lines = g.readlines()
                for proc, line in lines:
                    yield line

        return Response( read_process(), mimetype= 'text/plain')
    



api.add_resource(DbtCommand, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

