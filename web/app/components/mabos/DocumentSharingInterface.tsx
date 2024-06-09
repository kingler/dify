import React from 'react'

const DocumentSharingInterface: React.FC = () => {
  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (file) {
      const formData = new FormData()
      formData.append('file', file)

      try {
        const response = await fetch('http://localhost:5000/upload', {
          method: 'POST',
          body: formData,
          credentials: 'include', // Include cookies or authorization headers if needed
        })
        if (response.ok) {
          console.log('File uploaded successfully');
        } else {
          console.error('Upload failed');
        }
      } catch (error) {
        console.error('Error:', error)
      }
    }
  }

  const handleFileDownload = async (fileName: string) => {
    try {
      const response = await fetch(`http://localhost:5000/download/${fileName}`)
      if (response.ok) {
        const blob = await response.blob()
        const downloadUrl = window.URL.createObjectURL(blob)
        const link = document.createElement('a')
        link.href = downloadUrl
        link.download = fileName
        document.body.appendChild(link)
        link.click()
        link.remove()
      } else {
        console.error('Download failed')
      }
    } catch (error) {
      console.error('Error:', error)
    }
  }

  return (
    <div>
      <h2>Document Sharing</h2>
      <input type="file" onChange={handleFileUpload} />
      <button onClick={() => handleFileDownload('example.pdf')}>Download Example File</button>
      {/* Implement other features as described */}
    </div>
  )
}

export default DocumentSharingInterface
