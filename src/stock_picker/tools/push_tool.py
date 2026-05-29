from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class PushNotification(BaseModel):
    """A message to be sent to the user"""
    message: str = Field(..., description="The message to be sent to the user.")

class PushNotificationTool(BaseTool):
    _sent: bool = False

    name: str = "Send a Push Notification"
    description: str = (
        "This tool is used to send a push notification to the user."
    )
    args_schema: Type[BaseModel] = PushNotification

    def _run(self, message: str) -> str:
        pushover_user = os.getenv("PUSHOVER_USER")
        pushover_token = os.getenv("PUSHOVER_TOKEN")

        if not pushover_user: return "ERROR: PUSHOVER_USER missing" 
        if not pushover_token: return "ERROR: PUSHOVER_TOKEN missing"

        pushover_url = "https://api.pushover.net/1/messages.json"

        payload = { "user": pushover_user, "token": pushover_token, "title": "CrewAI Alert", "message": message, } 
        print(f"Sending payload: {payload}")

        try:
            
            if PushNotificationTool._sent:
                return "Notification already sent. Skipping duplicate."
            PushNotificationTool._sent = True

            response = requests.post(pushover_url, data=payload)
            print(f"Status Code: {response.status_code}") 
            print(f"Response Text: {response.text}") 
            response.raise_for_status() 
            return f"Notification sent successfully: {message}" 
        except Exception as e: 
            print(f"Pushover Error: {str(e)}")
            return f"Notification failed: {str(e)}"

    @classmethod
    def reset(cls):
        cls._sent = False