// Dashboard.tsx
import React from 'react'
import { CartesianGrid, Line, LineChart, Tooltip, XAxis, YAxis } from '@recharts'

const Dashboard: React.FC = () => {
  const data = [
    { name: 'Jan', value: 100 },
    { name: 'Feb', value: 120 },
    { name: 'Mar', value: 110 },
    { name: 'Apr', value: 130 },
    { name: 'May', value: 125 },
    { name: 'Jun', value: 115 },
    { name: 'Jul', value: 140 },
    { name: 'Aug', value: 135 },
    { name: 'Sep', value: 120 },
    { name: 'Oct', value: 125 },
    { name: 'Nov', value: 130 },
    { name: 'Dec', value: 140 },
  ]

  return (
    <div>
      <h2>Monitoring and Analytics</h2>
      <LineChart width={800} height={400} data={data}>
        <Line type="monotone" dataKey="value" stroke="#8884d8" />
        <CartesianGrid stroke="#ccc" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
      </LineChart>
    </div>
  )
}

export default Dashboard
