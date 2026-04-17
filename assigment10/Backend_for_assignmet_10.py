from flask import Flask, jsonify
import json

app = Flask(__name__)

# --- Task 4: Airport Lookup ---
@app.route('/airport/<code>')
def airport(code):
    
    icao_code = code.upper()
    try:
        with open('airports.json', 'r') as f:
            data = json.load(f)
            
            if icao_code not in data:
                
                return jsonify({"error": "Airport not found"}), 404
            
            store_code = {
                "icao": icao_code,
                "name": data[icao_code]['name'],
                "city": data[icao_code]['city'],
                "country": data[icao_code]['country']
            }
            return jsonify(store_code)
    except FileNotFoundError:
        return jsonify({"error": "Database file not found"}), 500

# --- Task 3: Prime Number Service ---
@app.route('/prime_number/<number>')
def prime_number(number):
    try:
        
        num = int(float(number))
        
        
        if num < 2:
            is_prime = False
        else:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
        
        return jsonify({
            "Number": num,
            "isPrime": is_prime
        })
    except ValueError:
        return jsonify({"error": "Invalid number provided"}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)