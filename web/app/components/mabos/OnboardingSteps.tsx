import React, { useState } from 'react'

// Replace with your actual API endpoint
const API_ENDPOINT = '/api/business' // Replace with your actual API endpoint

/**
 * OnboardingSteps Component for collecting initial business information.
 * @returns {JSX.Element} - The rendered onboarding steps form.
 */
const OnboardingSteps = () => {
  const [businessName, setBusinessName] = useState('')
  const [businessType, setBusinessType] = useState('')
  const [businessAddress, setBusinessAddress] = useState('')
  const [businessPhone, setBusinessPhone] = useState('')
  const [businessEmail, setBusinessEmail] = useState('')

  const handleInputChange = setter => (event) => {
    /**
     * Generic input change handler.
     * @param {function} setter - The state setter function.
     * @param {Event} event - The input change event.
     */
    setter(event.target.value)
  }

  const handleSubmit = async (event) => {
    event.preventDefault()

    try {
      const response = await fetch(API_ENDPOINT, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          businessName,
          businessType,
          businessAddress,
          businessPhone,
          businessEmail,
        }),
      })

      if (response.ok) {
        // Handle success, e.g., redirect to the next step or show a success message
        console.log('Business information submitted successfully')
      }
      else {
        console.error('Failed to submit business information')
      }
    }
    catch (error) {
      console.error('An error occurred:', error)
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h1>Welcome to the Onboarding Process</h1>
      <p>We will guide you through setting up your business.</p>
      <div>
        <label htmlFor="businessName">Business Name:</label>
        <input type="text" id="businessName" value={businessName} onChange={handleInputChange(setBusinessName)} placeholder="Enter your business name" required />
      </div>
      <div>
        <label htmlFor="businessType">Business Type:</label>
        <input type="text" id="businessType" value={businessType} onChange={handleInputChange(setBusinessType)} placeholder="Enter your business type" required />
      </div>
      <div>
        <label htmlFor="businessAddress">Business Address:</label>
        <input type="text" id="businessAddress" value={businessAddress} onChange={handleInputChange(setBusinessAddress)} placeholder="Enter your business address" required />
      </div>
      <div>
        <label htmlFor="businessPhone">Business Phone:</label>
        <input type="tel" id="businessPhone" value={businessPhone} onChange={handleInputChange(setBusinessPhone)} placeholder="Enter your business phone number" required />
      </div>
      <div>
        <label htmlFor="businessEmail">Business Email:</label>
        <input type="email" id="businessEmail" value={businessEmail} onChange={handleInputChange(setBusinessEmail)} placeholder="Enter your business email" required />
      </div>
      <button type="submit">Next</button>
    </form>
  )
}

export default OnboardingSteps
