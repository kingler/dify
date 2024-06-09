// Frontend (AgentConfiguration.tsx)
const _handleAddAgent = async () => {
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
export default AgentConfiguration
