class Team:
    ...

    def assign_task(self, task):
        for agent in self.agents:
            if agent.can_handle(task):
                goal = self.create_goal(task)
                agent.make_decision(goal)
                break

    def receive_feedback(self, feedback):
        for agent in self.agents:
            agent.receive_feedback(feedback)