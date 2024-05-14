import React, { useState } from 'react'
const OnboardingPage = () => {
  const [businessIdea, setBusinessIdea] = useState('')
  const [productService, setProductService] = useState('')

  const handleSubmit = async () => {
    const userData = {
      business_idea: businessIdea,
      product_service: productService,
    }

    // Send user data to backend for processing
    await fetch('/api/onboarding', {
      method: 'POST',
      body: JSON.stringify(userData),
    })
  }

  return (
    <div>
      <h2>Onboarding</h2>
      <input
        type="text"
        placeholder="Business Idea"
        value={businessIdea}
        onChange={e => setBusinessIdea(e.target.value)}
      />
      {/* ... */}
    </div>
  )
}
