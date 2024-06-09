// BusinessProfile.tsx
import React, { useState } from 'react'

const BusinessProfile: React.FC = () => {
  const [_formData, _setFormData] = useState({
    description: '',
    goals: '',
    targetMarket: '',
    // Add more fields as needed
  })

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // Handle form submission logic
  }

  return (
    <div>
      <h2>Business Profile Setup</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="description">Description:</label>
        <input
          type="text"
          id="description"
          value={_formData.description}
          onChange={e => _setFormData({ ..._formData, description: e.target.value })}
        />

        <label htmlFor="goals">Goals:</label>
        <input
          type="text"
          id="goals"
          value={_formData.goals}
          onChange={e => _setFormData({ ..._formData, goals: e.target.value })}
        />

        <label htmlFor="targetMarket">Target Market:</label>
        <input
          type="text"
          id="targetMarket"
          value={_formData.targetMarket}
          onChange={e => _setFormData({ ..._formData, targetMarket: e.target.value })}
        />
        <button type="submit">Save Profile</button>
      </form>
    </div>
  )
}

export default BusinessProfile
