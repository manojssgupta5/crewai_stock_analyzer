
from dotenv import load_dotenv

# pyrefly: ignore [missing-import]
from push_tool import PushNotificationTool

load_dotenv()

tool = PushNotificationTool()
result = tool._run("Stock alert test")

print(result)
