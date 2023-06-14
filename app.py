from flask import Flask, request
from flask_restful import Resource, Api
import subprocess


app = Flask(__name__)
api = Api(app)

# TODO log to client

class DbtCommand(Resource):
    def post(self):
        request_data = request.get_json(force=True)
        dbt_cmd = request_data['dbt']
        run_cmd = subprocess.run(f'dbt {dbt_cmd}', shell=True)
        if run_cmd.returncode != 0:
            return {
                'message': f'Command: << dbt {dbt_cmd} >> failed with return code {run_cmd.returncode}. Please '
                            f'check the web server logs for more information on the error.\n'
                            # f'{run_cmd.stdout}'
                            }, 400
        return {
            'message': f'Command: << dbt {dbt_cmd} >> ran successfully with return code 0.\n'
            # f'{run_cmd.stdout}'
            }, 200


api.add_resource(DbtCommand, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
