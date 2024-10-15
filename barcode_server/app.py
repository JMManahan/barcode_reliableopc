from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan_barcode():
    # Get the scanned data from the request
    data = request.json
    barcode_id = data.get('barcode_id')
    
    # Process the barcode (you can add database lookup here)
    response = {
        "message": f"Received barcode: {barcode_id}",
        "status": "success"
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
