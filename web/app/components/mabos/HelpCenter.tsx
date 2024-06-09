// HelpCenter.tsx
import React from 'react'

const HelpCenter: React.FC = () => {
  return (
    <div>
      <h2>Help and Support</h2>
      {/* Render help center UI */}
      <h3>FAQs</h3>
      <ul>
        <li>How do I create a new agent?</li>
        <li>How do I configure my business processes?</li>
        <li>How do I set up integrations with other systems?</li>
      </ul>
      <h3>Tutorials</h3>
      <ul>
        <li>Getting started with the Dify Multi-Agent IDE</li>
        <li>Configuring agents and business processes</li>
        <li>Integrating with external systems</li>
      </ul>
      <h3>Support</h3>
      <p>Contact our support team at <a href="mailto:support@dify.com">support@dify.com</a> for any questions or issues.</p>
    </div>
  )
}

export default HelpCenter
