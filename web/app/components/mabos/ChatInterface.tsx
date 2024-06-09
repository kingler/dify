import React from 'react'

const ChatInterface: React.FC = () => {
  return (
    <div>
      <h2>Chat</h2>
      <p>Interface for team communication.</p>
      <div className="chat-container">
        <ul className="message-list">
          {/* Messages will be mapped here */}
        </ul>
        <div className="input-area">
          <input type="text" placeholder="Type a message..." />
          <button>Send</button>
        </div>
      </div>
    </div>
  )
}

export default ChatInterface
