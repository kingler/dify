import type { Collaboration, Dashboard, DataIntegration, DocumentDetails, GoalDetails } from '@/types/mabos'

export type MabosModel = {
  documentDetails: DocumentDetails
  collaboration: Collaboration
  dashboard: Dashboard
  dataIntegration: DataIntegration
  goalDetails: GoalDetails
}

export const fetchMabosData = async (endpoint: string): Promise<MabosModel> => {
  try {
    const response = await fetch(endpoint)
    if (!response.ok) throw new Error('Failed to fetch Mabos data')
    return await response.json() as MabosModel
  } catch (error) {
    console.error('Error fetching Mabos data:', error)
    throw error
  }
}
