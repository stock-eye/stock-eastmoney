from flask import request, Flask
import eastmoney as em

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/groups')
def get_route():
    em.get_groups()
    return "success"


@app.route('/group/<group_name>', methods=['POST'])
def create_route(group_name):
    try:
        em.create_group(group_name)
    except Exception as e:
        print(e)
        return "failed"
    return "succeed"


@app.route('/group/<group_name>', methods=['DELETE'])
def delete_route(group_name):
    try:
        em.del_group(group_name)
    except Exception as e:
        print(e)
        return "failed"
    return "succeed"


@app.route('/group/<group_name>/code/<code>', methods=['PUT'])
def add_to_group(group_name, code):
    try:
        em.add_to_group(code, group_name=group_name)
    except Exception as e:
        print(e)
        return "failed"
    return "succeed"


if __name__ == '__main__':
    app.run(port=8080)
