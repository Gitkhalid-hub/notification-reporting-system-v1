# THE NOTIFICATION CREATION, SAVING, AND LOADING STAGE
import json
from datetime import datetime

class NotificationHistory:
	
	def load_history(self, history_path):
		
		if not history_path.exists():
			return []
		
		if history_path.stat().st_size == 0:
			return []
		
		with open(history_path, "r") as file:
			notification_history = json.load(file)
			
		return notification_history
	
	def create_record(self, message, status):
		
		if message == "":
			raise Exception(f"Message cannot be empty! -> {message}")
		
		if status not in ("success", "failure"):
			raise Exception(f"{status} must be either 'success' or 'failure'")
		
		notification_record = {
			"message": message,
			"status": status,
			"timestamp": str(datetime.now())
		}
		
		return notification_record
	
	def save_record(self, history_path, record):
		
		# Create logs/ folder if it does not exist
		history_path.parent.mkdir(
			parents= True,
			exist_ok= True
		)
		
		# Load existing notification history from JSON
		history = self.load_history(history_path)
		
		# Add the new record to the history list
		history.append(record)
		
		# Write the updated history list back to JSON
		with open(history_path, "w") as file:
			json.dump(history, file, indent=4)
		
		return history