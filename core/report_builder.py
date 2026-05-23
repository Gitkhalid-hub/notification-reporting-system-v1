# THE DATA DETECTION STAGE.

class ReportBuilder:
	
	def build_report(self, analytics_data):
		
		if analytics_data == "":
			raise Exception(f"Analytics data cannot be empty: {analytics_data}")
		
		total_events = analytics_data["total_events"]
		successful_events = analytics_data["successful_events"]
		failed_events = analytics_data["failed_events"]
		most_used_tool = analytics_data["most_used_tool"]
		
		reported_text = f"""
		NOTIFICATION AND REPORTING SYSTEM

		Total Events: {total_events}
		Successful Events: {successful_events}
		Failed Events: {failed_events}
		Most Used Tool: {most_used_tool}
		"""
		
		return reported_text