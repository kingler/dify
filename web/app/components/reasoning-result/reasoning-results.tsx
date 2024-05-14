const ReasoningResults = ({ results, onFeedback }) => {
  const handleFeedback = (feedback) => {
    onFeedback(feedback)
  }

  return (
    <div>
      <h3>Reasoning Results</h3>
      {/* Display reasoning results */}
      <button onClick={() => handleFeedback('positive')}>Positive Feedback</button>
      <button onClick={() => handleFeedback('negative')}>Negative Feedback</button>
    </div>
  )
}
