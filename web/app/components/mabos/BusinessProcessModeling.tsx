// BusinessProcessModeling.tsx
import React, { useState } from 'react'
import { BusinessProcessModelingComponent } from './BusinessProcessModelingComponent'

const BusinessProcessModeling: React.FC = () => {
  const [processes, setProcesses] = useState([])

  const handleAddProcess = () => {
    // Handle adding a new process
    setProcesses([...processes, { id: processes.length, name: `Process ${processes.length + 1}` }])
  }

  return (
    <div>
      <h2>Business Process Modeling</h2>
      <BusinessProcessModelingComponent processes={processes} />
      <button onClick={handleAddProcess}>Add Process</button>
    </div>
  )
}

export default BusinessProcessModeling
