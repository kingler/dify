/* eslint-disable no-tabs */
import { fetchWithTimeout } from './fetchUtil'

export class MabosService {
  static async getDocumentDetails(documentId: string) {
	try {
		const response = await fetchWithTimeout(`/api/mabos/documents/${documentId}`, {
			method: 'GET',
		})
		if (!response.ok) throw new Error('Network response was not ok')
		return await response.json()
	} catch (error) {
		console.error('Failed to fetch document details:', error)
		throw error
	}
}

  // Add more methods as needed for other MABOS functionalities
}
