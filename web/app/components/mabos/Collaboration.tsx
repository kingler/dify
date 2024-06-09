// Collaboration.tsx
import React from 'react'
import ChatInterface from './ChatInterface' // Adjust the path as necessary
import DocumentSharingInterface from './DocumentSharingInterface' // Adjust the path as necessary
import NotificationsSetupInterface from './NotificationsSetupInterface' // Adjust the path as necessary

const Collaboration: React.FC = () => {
  return (
    <div>
      <h2>Collaboration and Communication</h2>
      <div className="collaboration-ui">
        <h3>Messaging and Chat</h3>
        <div className="chat-interface">
          <ChatInterface />
        </div>
        <h3>Document Sharing</h3>
        <div className="document-sharing-interface">
          <DocumentSharingInterface />
        </div>
        <h3>Notifications and Alerts</h3>
        <div className="notification-setup">
          <NotificationsSetupInterface />
        </div>
      </div>
    </div>
  )
}

export default Collaboration
