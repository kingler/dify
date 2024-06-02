from mabos.interfaces.mabos_api import MABOSRequest, MABOSResponse

@app.route('/api/mabos/createUser', methods=['POST'])
def create_user():
    request_data = MABOSRequest(**request.json)
    # Process the request and create the response
    response_data = MABOSResponse(status='success', data=response_payload)
    return jsonify(response_data.__dict__)

# ... other API endpoints