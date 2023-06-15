from flask import Flask, request
from flask_restful import Resource, Api
import subprocess

app = Flask(__name__)
api = Api(app)


class DbtCommand(Resource):
    def post(self):
        request_data = request.get_json(force=True)
        dbt_cmd = request_data['dbt']
        run_cmd = subprocess.run(f'dbt {dbt_cmd}', shell=True, capture_output=True)
        output = run_cmd.stdout.decode("utf-8")
        if run_cmd.returncode != 0:
            return output, 400

        return output, 200


api.add_resource(DbtCommand, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
