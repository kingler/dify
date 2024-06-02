44 directories, 115 files

---

├── agents
│   ├── __init__.py
│   ├── agent.py
│   ├── coordinator_agents
│   │   ├── business_process_manager.py
│   │   └── goal_model_agent.py
│   ├── information_agents
│   │   ├── data_management_agent.py
│   │   └── ontology_agent.py
│   ├── interface_agents
│   │   └── onboarding_agent.py
│   ├── supervisor_agents
│   │   ├── enterprise_architecture_agent.py
│   │   └── security_agent.py
│   ├── task_agents
│   │   ├── business_plan_agent.py
│   │   └── reporting_agent.py
│   └── worker_agents
├── bdi
│   ├── __init__.py
│   ├── belief.py
│   ├── desire.py
│   └── intention.py
├── communication
│   ├── __init__.py
│   ├── broker.py
│   ├── communication.md
│   ├── communication.py
│   ├── communication_ontology.py
│   ├── delayed_message_queue.py
│   ├── group_formation.py
│   ├── message.py
│   ├── message_encryptor.py
│   ├── message_serializer.py
│   ├── message_storage.py
│   └── negotiation
│       ├── auction_based_negotiation.py
│       ├── contract_net_protocol.py
│       ├── integrative_negotiation.py
│       └── multi_issue_negotiation.py
├── configuration
│   ├── __init__.py
│   └── configuration_manager.py
├── data_management
│   ├── __init__.py
│   ├── backup_exceptions.py
│   ├── backup_purger.py
│   ├── backup_scheduler.py
│   ├── backup_storage.py
│   ├── data.py
│   ├── data_backup_manager.py
│   ├── data_mapper.py
│   ├── data_store
│   │   └── data_storage.py
│   ├── data_transformation_manager.py
│   ├── data_validation_manager.py
│   └── repositories
│       ├── process_definition_repository.py
│       ├── process_instance_repository.py
│       └── repository_base.py
├── error_handler.py
├── event_management
│   └── event.py
├── goal_management
│   ├── goal.md
│   └── goal.py
├── interfaces
│   ├── __init__.py
│   └── mabos-api.py
├── knowledge_management
│   ├── __init__.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── knowledge_base.py
│   │   └── knowledge_graph.py
│   ├── debugging
│   │   └── reasoning_debugger.py
│   ├── explainable_ai
│   │   └── reasoning_explainer.py
│   ├── knowledge_base
│   │   ├── best_practices
│   │   │   └── __init__.py
│   │   ├── industry_standards
│   │   │   └── __init__.py
│   │   └── process_templates
│   │       ├── __init__.py
│   │       └── process_template.py
│   ├── knowledge_extraction
│   │   └── __init__.py
│   ├── knowledge_integration
│   │   └── __init__.py
│   ├── learning
│   │   └── reasoning_learner.py
│   ├── logging
│   │   └── reasoning_logger.py
│   ├── ontology
│   │   ├── __init__.py
│   │   ├── meta_ontology.ttl
│   │   ├── ontology.py
│   │   └── ontology.ttl
│   ├── reasoning
│   │   ├── case_based_reasoner.py
│   │   ├── goal_plan_tree.py
│   │   └── htn_planner.py
│   ├── reasoning_engine.py
│   └── utils
│       ├── __init__.py
│       ├── caching.py
│       └── indexing.py
├── localization
│   └── localization_manager.py
├── logging
│   ├── __init__.py
│   └── logger.py
├── main.py
├── monitoring
│   ├── __init__.py
│   ├── anomaly_detection_engine.py
│   ├── monitoring.py
│   ├── performance_metrics_collector.py
│   └── predictive_analytics_engine.py
├── onboarding.py
├── planning
│   ├── __init__.py
│   ├── plan.md
│   └── plan.py
├── process_management
│   ├── __init__.py
│   ├── business_process_manager.py
│   ├── services
│   │   ├── __init__.py
│   │   └── process_optimization_engine.py
│   └── utils
│       ├── __init__.py
│       ├── bottleneck_identifier.py
│       ├── inefficiency_identifier.py
│       ├── optimization_suggestion_generator.py
│       ├── performance_metrics_calculator.py
│       └── suggestion_prioritizer.py
├── skills
│   ├── __init__py
│   └── skills.py
├── task_management
│   ├── __init__.py
│   ├── action.py
│   ├── task.py
│   ├── task_manager.py
│   └── task_output.py
├── temp.txt
├── user_interface.py
├── user_management
│   ├── __init__.py
│   ├── authentication_manager.py
│   ├── authorization_manager.py
│   └── user.py
└── visualization
    ├── __init__.py
    └── data_visualization_manager.py