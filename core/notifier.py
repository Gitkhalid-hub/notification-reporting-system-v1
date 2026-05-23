# THE DISPLAY STAGE.

class Notifier:
	
	def notify(self, message):
		
		if message == "":
			raise Exception(f"Message cannot be empty: {message}")
		
		print(message)
		
		return message