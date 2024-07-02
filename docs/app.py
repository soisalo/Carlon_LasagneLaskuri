from flask import Flask, jsonify, request, send_from_directory
from lasagne_laskuri import LasagneLaskuri

app = Flask(__name__)
laskuri = LasagneLaskuri()
laskuri.load_from_file("lasagne.txt")

@app.route('/')
def index():
    return app.send_from_directory('static', 'index.html')

@app.route('/add_lasagne', methods=['GET'])
def add_lasagne():
    portions = int(request.args.get('portions', 1))
    laskuri.add_lasagne_portion(portions)
    laskuri.save_to_file("lasagne.txt")
    return jsonify(laskuri.get_totals())

if __name__ == '__main__':
    app.run(debug=True)
