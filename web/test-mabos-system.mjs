import { MabosService } from '../service/mabos_service'

const testMultiAgentSystemInstantiation = async (businessDescription) => {
  try {
    const agents = await MabosService.instantiateMultiAgentSystem(businessDescription)
    console.log(`MultiAgent System instantiated based on business type: ${businessDescription.businessType}`)
    return agents
  } catch (error) {
    console.error('Failed to instantiate MultiAgent System:', error)
    process.exit(1)
  }
}

const verifyActiveAgents = async (businessDescription) => {
  try {
    const agents = await testMultiAgentSystemInstantiation(businessDescription)
    if (agents.every(agent => agent.isActive)) {
      console.log('All agents in the system are active.')
    } else {
      console.error('Some agents in the system are not active.')
      process.exit(1);
    }
  } catch (error) {
    console.error('Error during agent verification:', error)
    process.exit(1)
  }
}

// Example business description input
const businessDescription = {
  businessName: 'Tech Innovations Inc.',
  businessType: 'Technology',
  businessAddress: '123 Tech Lane',
  businessPhone: '555-1234',
  businessEmail: 'contact@techinnovations.com',
}

verifyActiveAgents(businessDescription)
