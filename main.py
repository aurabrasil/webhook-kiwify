from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

SMM_API_URL = "https://exemplo-provedor.com/api/v2"  
SMM_API_KEY = os.getenv("SMM_API_KEY", "COLOQUE_SEU_TOKEN_AQUI")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    try:
        order_data = {
            "key": SMM_API_KEY,
            "action": "add",
            "service": 1,  
            "link": data.get("customer_email"),
            "quantity": 100
        }

        response = requests.post(SMM_API_URL, data=order_data)
        return jsonify({"status": "success", "smm_response": response.json()}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
