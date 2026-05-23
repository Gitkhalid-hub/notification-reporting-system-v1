# THE STORAGE AND LOADING STAGE.

class ReportStorage:
	
	def save_report(self, report_path, report_text):
		
		# create reports folder if it does not exist
		report_path.parent.mkdir(parents=True, exist_ok=True)
		
		with open(report_path, "w") as file:
			file.write(report_text)
			
		return report_path
	
	def load_report(self, report_path):
		
		if not report_path.exists():
			raise Exception(f"Report file must exist.")
		
		with open(report_path, "r") as file:
			report_text = file.read()
			
			return report_text