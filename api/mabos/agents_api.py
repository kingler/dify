from flask import request, jsonify
from mabos.interfaces.mabos_api import MABOSRequest, MABOSResponse
from mabos.agents.agent import Agent

@app.route('/api/mabos/agents', methods=['POST'])
def create_agent():
    request_data = MABOSRequest(**request.json)
    # Logic to create a new agent
    new_agent = Agent(**request_data.data)
    # Save the new agent to the database or appropriate storage
    response_data = MABOSResponse(status='success', data=new_agent.__dict__)
    return jsonify(response_data.__dict__)

@app.route('/api/mabos/agents', methods=['GET'])
def get_agents():
    # Logic to retrieve all agents
    agents_list = [agent.__dict__ for agent in Agent.query.all()]
    response_data = MABOSResponse(status='success', data=agents_list)
    return jsonify(response_data.__dict__)

@app.route('/api/mabos/agents/<agent_id>', methods=['PUT'])
def update_agent(agent_id):
    request_data = MABOSRequest(**request.json)
    # Logic to update an existing agent
    agent = Agent.query.filter_by(agent_id=agent_id).first()
    if agent:
        agent.update(**request_data.data)
        response_data = MABOSResponse(status='success', data=agent.__dict__)
    else:
        response_data = MABOSResponse(status='error', message='Agent not found')
    return jsonify(response_data.__dict__)

@app.route('/api/mabos/agents/<agent_id>', methods=['DELETE'])
def delete_agent(agent_id):
    # Logic to delete an agent
    agent = Agent.query.filter_by(agent_id=agent_id).first()
    if agent:
        agent.delete()
        response_data = MABOSResponse(status='success', message='Agent deleted')
    else:
        response_data = MABOSResponse(status='error', message='Agent not found')
    return jsonify(response_data.__dict__)
