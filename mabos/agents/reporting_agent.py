# mabos/agents/reporting_agent.py
from ..task_management.task import Task

class ReportingAgent:
    def __init__(self, data_store, visualization_manager):
        self.data_store = data_store
        self.visualization_manager = visualization_manager
        # Initialize other attributes and components

    def generate_report(self, report_type, parameters):
        data = self.data_store.retrieve_data(report_type, parameters)
        return self.visualization_manager.generate_report(data, report_type)

    def schedule_report(self, report_type, parameters, schedule):
        report_task = Task(
            name=f"Generate {report_type} Report",
            description=f"Generate a {report_type} report with parameters: {parameters}",
            function=self.generate_report,
            args=(report_type, parameters),
            schedule=schedule
        )
        
        # Add the report task to the agent's task queue
        self.agent.add_task(report_task)
