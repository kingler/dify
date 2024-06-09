// GoalSetting.tsx
import React, { useState } from 'react'
import GoalDetails from './GoalDetails' // Adjust the path as necessary based on your project structure

const GoalSetting: React.FC = () => {
  const [goals, setGoals] = useState([])

  const handleAddGoal = () => {
    // Handle adding a new goal
    // Implement the logic to add a new goal to the state
    // For example:
    const newGoal = {
      id: Math.random().toString(),
      description: '',
      target: '',
      deadline: '',
      priority: 0,
      goal_type: '',
      preconditions: [],
      postconditions: [],
      effects: [],
      metrics: [],
      parent_goal: null,
      sub_goals: [],
      status: 'pending',
    }
    setGoals([...goals, newGoal])
  }

  return (
    <div>
      <h2>Goal and KPI Setting</h2>
      <div className="goal-setting-ui">
        <button onClick={handleAddGoal}>Add Goal</button>
      </div>
      <div className="goal-list">
        <ul>
          {goals.map((goal) => {
            return (
              <li key={goal.id}>
                <GoalDetails goal={goal} />
                <p>Description: {goal.description}</p>
                <p>Target: {goal.target}</p>
                <p>Deadline: {goal.deadline}</p>
                <p>Priority: {goal.priority}</p>
                <p>Type: {goal.goal_type}</p>
                <p>Status: {goal.status}</p>
              </li>
            )
          })}
        </ul>
      </div>
    </div>
  )
} // Closing brace for the GoalSetting function

export default GoalSetting
