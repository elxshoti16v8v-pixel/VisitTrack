from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
locations = {}

@app.route('/')
def home():
    return "VisitTrack Server is running!"

@app.route('/api/send_location', methods=['POST'])
def send_location():
    data = request.json
    visitor_id = data.get('id')
    lat = data.get('lat')
    lng = data.get('lng')
    if visitor_id and lat is not None and lng is not None:
        locations[visitor_id] = {'lat': float(lat), 'lng': float(lng)}
        return jsonify(success=True)
    return jsonify(success=False), 400

@app.route('/api/locations')
def get_locations():
    return jsonify(locations)

@app.route('/send')
def send_page():
    return render_template('send.html')

@app.route('/map')
def map_page():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
