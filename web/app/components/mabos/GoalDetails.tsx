import React from 'react'

type GoalProps = {
  goal: {
    id: number
    description: string
    target: string
    deadline: string
    priority: number
    goal_type: string
    preconditions: string[]
    postconditions: string[]
    effects: string[]
    metrics: string[]
    parent_goal: GoalProps['goal'] | null
    sub_goals: GoalProps['goal'][]
    status: string
  }
}

const GoalDetails: React.FC<GoalProps> = ({ goal }) => {
  return (
    <div>
      <h3>Goal Details</h3>
      <p>ID: {goal.id}</p>
      <p>Description: {goal.description}</p>
      <p>Target: {goal.target}</p>
      <p>Deadline: {goal.deadline}</p>
      <p>Priority: {goal.priority}</p>
      <p>Type: {goal.goal_type}</p>
      <p>Preconditions: {goal.preconditions.join(', ')}</p>
      <p>Postconditions: {goal.postconditions.join(', ')}</p>
      <p>Effects: {goal.effects.join(', ')}</p>
      <p>Metrics: {goal.metrics}</p>
      <p>Status: {goal.status}</p>
      <p>Parent Goal ID: {goal.parent_goal ? goal.parent_goal.id : 'None'}</p>
      <p>Sub Goals: {goal.sub_goals.map(sub => sub.id).join(', ')}</p>
    </div>
  )
}

export default GoalDetails
