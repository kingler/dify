import React, { useState } from 'react'

const OnboardingSteps = () => {
  const [businessName, setBusinessName] = useState('')
  const [businessType, setBusinessType] = useState('')
  const [businessAddress, setBusinessAddress] = useState('')
  const [businessPhone, setBusinessPhone] = useState('')
  const [businessEmail, setBusinessEmail] = useState('')

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault()
    // Here you would typically handle the submission to the backend
    console.log('Business Information:', { businessName, businessType, businessAddress, businessPhone, businessEmail })
    // Proceed to the next step or show a success message
  }

  return (
    <form onSubmit={handleSubmit}>
      <h1>Welcome to the Onboarding Process</h1>
      <p>We will guide you through setting up your business.</p>
      <input type="text" value={businessName} onChange={e => setBusinessName(e.target.value)} placeholder="Enter your business name" />
      <input type="text" value={businessType} onChange={e => setBusinessType(e.target.value)} placeholder="Enter your business type" />
      <input type="text" value={businessAddress} onChange={e => setBusinessAddress(e.target.value)} placeholder="Enter your business address" />
      <input type="text" value={businessPhone} onChange={e => setBusinessPhone(e.target.value)} placeholder="Enter your business phone number" />
      <input type="email" value={businessEmail} onChange={e => setBusinessEmail(e.target.value)} placeholder="Enter your business email" />
      <button type="submit">Submit</button>
    </form>
  )
}

export default OnboardingSteps
