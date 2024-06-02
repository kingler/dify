import { MABOSRequest, MABOSResponse } from '../types/mabos-api';

export interface MABOSRequest {
    action: string;
    payload: object;
  }
  
  export interface MABOSResponse {
    status: 'success' | 'error';
    data?: object;
    error?: string;
  }
