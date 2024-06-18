from .agents.agent import Agent
from .knowledge_management.ontology.ontology import Ontology
from .knowledge_management.knowledge_graph import KnowledgeGraph
from .knowledge_management.reasoning.reasoning_engine import ReasoningEngine
from .communication.communication import Communication
from .user_interface import UserInterface
from .goal_management import GoalManager
from .plan_management import PlanManager
from flask import Flask, request, jsonify

app = Flask(__name__)

def main():
    # Initialize the ontology and knowledge graph
    ontology = Ontology()
    knowledge_graph = KnowledgeGraph()

    # Initialize the agents
    agents = [
        Agent("agent1", ontology, knowledge_graph),
        Agent("agent2", ontology, knowledge_graph),
        # Add more agents as needed
    ]

    # Initialize the reasoning engine, communication, and user interface
    reasoning_engine = ReasoningEngine(ontology, knowledge_graph)
    communication = Communication()
    user_interface = UserInterface()

    # Initialize the goal and plan managers
    goal_manager = GoalManager()
    plan_manager = PlanManager()

    # Main loop
    while True:
        # Perform reasoning for each agent
        for agent in agents:
            reasoning_engine.reason(agent)
        # Handle communication between agents
        for sender in agents:
            for receiver in agents:
                if sender != receiver:
                    message = {"content": f"Update from {sender.agent_id}"}
                    communication.send_message(sender,receiver, message)

        # Update the user interface based on agent actions
        user_interface.update(agents)

        # Get user input and update agents accordingly
        user_commands = user_interface.get_user_input()
        for agent in agents:
            agent.update(user_commands)

        # Break the loop if a termination condition is met
        if user_interface.check_termination_condition():
            break

    # API routes for goal and plan management
    @app.route('/goals', methods=['POST'])
    def create_goal():
        data = request.get_json()
        goal = goal_manager.create_goal(data)
        return jsonify(goal)

    @app.route('/goals/<goal_id>', methods=['PUT'])
    def update_goal(goal_id):
        data = request.get_json()
        goal = goal_manager.update_goal(goal_id, data)
        return jsonify(goal)

    @app.route('/goals/<goal_id>', methods=['GET'])
    def get_goal(goal_id):
        goal = goal_manager.get_goal(goal_id)
        return jsonify(goal)

    @app.route('/plans', methods=['POST'])
    def create_plan():
        data = request.get_json()
        plan = plan_manager.create_plan(data)
        return jsonify(plan)

    @app.route('/plans/<plan_id>', methods=['PUT'])
    def update_plan(plan_id):
        data = request.get_json()
        plan = plan_manager.update_plan(plan_id, data)
        return jsonify(plan)

    @app.route('/plans/<plan_id>', methods=['GET'])
    def get_plan(plan_id):
        plan = plan_manager.get_plan(plan_id)
        return jsonify(plan)

if __name__ == "__main__":
    app.run()
