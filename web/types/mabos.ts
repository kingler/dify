export type MABOSRequest = {
  action: string
  payload: object
}

export type MABOSResponse = {
  status: 'success' | 'error'
  data?: object
  error?: string
}

export type AgentConfiguration = {
  id: string
  name: string
  role: string
  capabilities: string[]
}

export type BusinessProcessModeling = {
  processes: {
    id: number
    name: string
  }[]
}

export type BusinessProfile = {
  description: string
  goals: string
  targetMarket: string
}

export type Integration = {
  id: number
  name: string
}

export type DocumentDetails = {
  id: string
  title: string
  content: string
}

export type ChatInterface = {
  messages: string[]
  sendMessage: (message: string) => void

}

export type Collaboration = {
  chatInterface: ChatInterface
  documentSharingInterface: DocumentSharingInterface
  notificationsSetupInterface: NotificationsSetupInterface

}

export type Dashboard = {
  widgets: string[]
  dataSources: string[]
  visualizationTypes: string[]
}

export type DataIntegration = {
  integrationMethods: string[]
  dataSources: string[]
  dataDestinations: string[]
  dataTransformationCapabilities: string[]
}

export type DocumentSharingInterface = {
  sharingEnabled: boolean
  maxFileSizeMB: number
  allowedFileTypes: string[]
}

export type GoalDetails = {
  id: number
  description: string
  target: string
  deadline: string
  priority: number
  goal_type: string
  preconditions: string[]
  postconditions: string[]
  effects: string[]
  metrics: string
  parent_goal: Goal | null
  sub_goals: Goal[]
  status: string
}

export type GoalSetting = {
  id: string
  description: string
  target: string
  deadline: string
  priority: number
  goal_type: string
  preconditions: string[]
  postconditions: string[]
  effects: string[]
  metrics: string
  parent_goal: Goal | null
  sub_goals: Goal[]
  status: string
}

export type HelpCenter = {
  faqs: string[]
  tutorials: string[]
  supportContactEmail: string
}

export type NotificationsSetupInterface = {
  emailNotificationsEnabled: boolean
  smsNotificationsEnabled: boolean
  pushNotificationsEnabled: boolean
  notificationFrequency: 'immediate' | 'daily' | 'weekly'
  notificationChannels: string[]

}
