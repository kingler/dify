from .onboarding import Onboarding

def main():
    ...
    user_data = ...  # Define user_data with appropriate value
    onboarding = Onboarding()
    agents, tools, knowledge = onboarding.generate_mas(user_data)
    ...