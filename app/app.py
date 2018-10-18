from flask import Flask, jsonify, abort, make_response, request, url_for


################ Initialization params ################

application = Flask(__name__)
application.config['JSON_AS_ASCII'] = False

#######################################################


## 'about' method
@application.route('/api/v1.0/about', methods=['GET'])
def about():
    return make_response(jsonify({'about': 'This is a RESTful test harness for Tikal'}), 200)
    

## jsonified error request for get_task method
@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080, debug=False)
#    application.run(host='127.0.0.1', port=8080, debug=True)
