from typing import Dict, Optional

class MABOSRequest:
    def __init__(self, action: str, payload: Dict):
        self.action = action
        self.payload = payload

class MABOSResponse:
    def __init__(self, status: str, data: Optional[Dict] = None, error: Optional[str] = None):
        self.status = status
        self.data = data
        self.error = error