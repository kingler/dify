# mabos/agents/business_plan_agent.py
from pydantic import BaseModel
from .utils_agents.broker import Broker

class BusinessPlanTemplate(BaseModel):
    executive_summary: str
    company_description: str
    market_analysis: dict
    organization_management: str
    service_product_line: str
    marketing_sales: str
    funding_request: str
    financial_projections: dict
    appendix: str

class BusinessPlanAgent:
    def __init__(self, location):
        self.location = location
        # Initialize other attributes and components

    def develop_business_plan(self, plan_details):
        # Directly return the comprehensive business plan using the template
        return BusinessPlanTemplate(
            executive_summary=plan_details.get('executive_summary', '...'),
            company_description=plan_details.get('company_description', '...'),
            market_analysis=plan_details.get('market_analysis', {}),
            organization_management=plan_details.get('organization_management', '...'),
            service_product_line=plan_details.get('service_product_line', '...'),
            marketing_sales=plan_details.get('marketing_sales', '...'),
            funding_request=plan_details.get('funding_request', '...'),
            financial_projections=plan_details.get('financial_projections', {}),
            appendix=plan_details.get('appendix', '...')
        )

    def send_message(self, recipient, message):
        broker = Broker()
        broker.register_agent(recipient, self.location)
        broker.route_message(self, recipient, message)