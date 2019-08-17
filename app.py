from flask import Flask, jsonify, abort, request, make_response

import init

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    """

    :param error:
    :return:
    """
    return make_response(jsonify({'error': 'Not Found'}), error.code)


@app.errorhandler(400)
def bad_request(error):
    """

    :param error:
    :return:
    """
    return make_response(jsonify({'error': 'Bad Request'}), error.code)


@app.route('/')
def root():
    """Serve root HTML file for single page application

    :return:
    """
    return app.send_static_file('index.html')


@app.route('/room/add/<room_number>', methods=['GET'])
def add_room(room_number):
    return jsonify({'room': room_number, 'status': 'added'})


@app.route('/room/remove/<room_number>', methods=['GET'])
def remove_room(room_number):
    return jsonify({'room': room_number, 'status': 'removed'})


@app.route('/room/active', methods=['GET'])
def active_participants():
    return jsonify({'participants': ['123', '456', '789']})


@app.route('/room/active/<room_number>', methods=['GET'])
def active_participants_for_room(room_number):
    return jsonify({'room': room_number, 'participants': ['123', '456', '789']})


@app.route('/room/call/transfer/<uuid>/<room_number>/false', methods=['GET'])
def transfer_participant(uuid, room_number):
    return jsonify({'uuid': uuid, 'room_number ': room_number})


@app.route('/room/summary/<room_number>', methods=['GET'])
def room_available(room_number):
    return jsonify({'room_number': room_number})


if __name__ == '__main__':
    host = init.PEXIP_SERVICE_HOST
    port = init.PEXIP_SERVICE_PORT

    init.logger.info('=' * 20)
    init.logger.info('Starting mock-pexip with parameters:')
    init.logger.info('PEXIP_SERVICE_HOST: {}'.format(init.PEXIP_SERVICE_HOST))
    init.logger.info('PEXIP_SERVICE_PORT: {}'.format(init.PEXIP_SERVICE_PORT))
    init.logger.info('=' * 20)

    app.run(host=host, port=int(port), debug=True)
