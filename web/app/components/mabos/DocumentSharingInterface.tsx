import React, { useEffect, useState } from 'react'
import { MabosService } from '../../services/MabosService'

import type { DocumentDetails } from '@/types/mabos'

const DocumentSharingInterface: React.FC = () => {
  const [documentDetails, setDocumentDetails] = useState<DocumentDetails | null>(null)

  useEffect(() => {
    const fetchDocumentDetails = async () => {
      try {
        const details = await MabosService.getDocumentDetails('123') // Example document ID
        setDocumentDetails(details)
      } catch (error) {
        console.error('Error fetching document details:', error)
      }
    }

    fetchDocumentDetails()
  }, [])

  return (
    <div>
      <h2>Document Sharing</h2>
      {documentDetails ? (
        <div>
          <h3>{documentDetails.title}</h3>
          <p>{documentDetails.content}</p>
        </div>
      ) : (
        <p>Loading document details...</p>
      )}
    </div>
  )
}

export default DocumentSharingInterface
