// Frontend (AgentConfiguration.tsx)
import React, { useState } from 'react'
import type { Agent } from '../../models/mabos'

const AgentConfiguration: React.FC = () => {
  const [newAgentName, setNewAgentName] = useState('')
  const [newAgentRole, setNewAgentRole] = useState('')
  const [newAgentCapabilities, setNewAgentCapabilities] = useState('')
  const [agents, setAgents] = useState<Agent[]>([])

  const handleAddAgent = async () => {
    const newAgent: Agent = {
      id: '',
      name: newAgentName,
      role: newAgentRole,
      capabilities: newAgentCapabilities.split(',').map(capability => capability.trim()),
    }

    try {
      const response = await fetch('/api/agents', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newAgent),
      })

      if (response.ok) {
        const createdAgent: Agent = await response.json()
        setAgents([...agents, createdAgent])
        setNewAgentName('')
        setNewAgentRole('')
        setNewAgentCapabilities('')
      } else {
        console.error('Failed to create agent')
      }
    } catch (error) {
      console.error('Error creating agent:', error)
    }
  }

  return (
    <div>
      <form onSubmit={handleAddAgent}>
        <h1>Add New Agent</h1>
        <div>
          <label htmlFor="agentName">Agent Name:</label>
          <input
            type="text"
            id="agentName"
            value={newAgentName}
            onChange={e => setNewAgentName(e.target.value)}
            placeholder="Enter agent name"
            required
          />
        </div>
        <div>
          <label htmlFor="agentRole">Agent Role:</label>
          <input
            type="text"
            id="agentRole"
            value={newAgentRole}
            onChange={e => setNewAgentRole(e.target.value)}
            placeholder="Enter agent role"
            required
          />
        </div>
        <div>
          <label htmlFor="agentCapabilities">Agent Capabilities:</label>
          <input
            type="text"
            id="agentCapabilities"
            value={newAgentCapabilities}
            onChange={e => setNewAgentCapabilities(e.target.value)}
            placeholder="Enter agent capabilities, separated by commas"
            required
          />
        </div>
        <button type="submit">Add Agent</button>
      </form>
    </div>
  )
}

export default AgentConfiguration
