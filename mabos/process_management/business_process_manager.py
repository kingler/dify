# mabos/process/business_process_manager.py
from mabos.knowledge_management.ontology.ontology import Ontology
from knowledge_management.knowledge_graph import KnowledgeGraph
from monitoring.performance_metrics_collector import PerformanceMetricsCollector
from monitoring.anomaly_detection_engine import AnomalyDetectionEngine
from monitoring.predictive_analytics_engine import PredictiveAnalyticsEngine

class BusinessProcessManager:
    """
    Class responsible for managing business processes.

    Attributes:
        broker (Broker): Reference to the broker component.
        process_definitions (dict): Dictionary to store process definitions.
        process_instances (dict): Dictionary to store active process instances.
        task_assignments (dict): Dictionary to store task assignments for agents.
        task_status (dict): Dictionary to store the status of tasks.
        process_monitoring_interval (int): Interval (in seconds) at which to monitor processes.
        ontology (Ontology): Reference to the ontology component.
        knowledge_graph (KnowledgeGraph): Reference to the knowledge graph component.
        performance_metrics_collector (PerformanceMetricsCollector): Reference to the performance metrics collector.
        anomaly_detection_engine (AnomalyDetectionEngine): Reference to the anomaly detection engine.
        predictive_analytics_engine (PredictiveAnalyticsEngine): Reference to the predictive analytics engine.
    """

    def __init__(self, broker):
        """
        Initialize the BusinessProcessManager.

        Args:
            broker (Broker): Reference to the broker component.
        """
        self.broker = broker
        # Initialize other attributes and components
        self.process_definitions = {}  # Dictionary to store process definitions
        self.process_instances = {}  # Dictionary to store active process instances
        self.task_assignments = {}  # Dictionary to store task assignments for agents
        self.task_status = {}  # Dictionary to store the status of tasks
        self.process_monitoring_interval = 60  # Interval (in seconds) at which to monitor processes
        self.ontology = Ontology()  # Reference to the ontology component
        self.knowledge_graph = KnowledgeGraph()  # Reference to the knowledge graph component
        self.performance_metrics_collector = PerformanceMetricsCollector(self)  # Reference to the performance metrics collector
        self.anomaly_detection_engine = AnomalyDetectionEngine(self.performance_metrics_collector)  # Reference to the anomaly detection engine
        self.predictive_analytics_engine = PredictiveAnalyticsEngine(self.performance_metrics_collector)  # Reference to the predictive analytics engine

    def rollback_process(self, process_instance_id):
        """
        Rollback the process execution to maintain system integrity.

        Args:
            process_instance_id (str): ID of the process instance to rollback.
        """
        if process_instance_id in self.process_instances:
            del self.process_instances[process_instance_id]
        for task_id in self.task_status.keys():
            if self.task_status[task_id] == 'assigned':
                self.task_status[task_id] = 'unassigned'
        self.broker.rollback_process(process_instance_id)
        print(f"Rolled back process {process_instance_id} due to execution failure.")

    def monitor_process(self, process_instance_id):
        """
        Monitor the progress of a process instance.

        Args:
            process_instance_id (str): ID of the process instance to monitor.
        """
        try:
            process_instance = self.process_instances[process_instance_id]
            task_assignments = process_instance['task_assignments']
            
            for agent_id, tasks in task_assignments.items():
                agent_location = self.broker.get_agent_location(agent_id)
                for task in tasks:
                    task_id = task['id']
                    task_status = self.broker.get_task_status(agent_id, task_id)
                    
                    if task_status == 'completed':
                        self.task_status[task_id] = 'completed'
                    elif task_status == 'failed':
                        self.task_status[task_id] = 'failed'
                        # Handle task failure
                    elif not task['is_critical']:
                        self.broker.send_delayed_message(agent_id, task_id, 'status_update')
            
            completed_tasks = [task for task, status in self.task_status.items() if status == 'completed']
            if len(completed_tasks) == len(process_instance['task_assignments']):
                process_instance['status'] = 'completed'
        except KeyError as e:
            raise KeyError(f"Key error accessing process data: {str(e)}") from e
        except Exception as e:
            raise RuntimeError(f"An error occurred while monitoring the process {process_instance_id}: {str(e)}") from e
