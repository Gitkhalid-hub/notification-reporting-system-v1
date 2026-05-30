# THE ORCHESTRATION STAGE.
import json
from pathlib import Path

from core.report_builder import ReportBuilder
from core.notifier import Notifier
from core.report_storage import ReportStorage
from core.notification_history import NotificationHistory


analytics_path = Path("sample_data/analytic_summary.json")
report_path = Path("reports/usage_report.txt")
notification_history_path = Path("logs/notification_history.json")

report_builder = ReportBuilder()
notifier = Notifier()
report_storage = ReportStorage()
notification_history = NotificationHistory()

try:
	with open(analytics_path, "r") as file:
		analytics_data = json.load(file)
		
		report_text = report_builder.build_report(analytics_data)
		
		saved_path = report_storage.save_report(report_path, report_text)
		
		notification_message = "Report generated successfully"
		
		notifier.notify(notification_message)
		
		notification_record = notification_history.create_record(
			notification_message,
		    "success"
		)
		
		notification_history.save_record(
			notification_history_path,
		    notification_record
		)
		
		print("\n=== FINAL SUMMARY ===")
		
		print("Report saved to:", saved_path)
		
		print("Notification status: SENT")
		
		print("History Location:", notification_history_path)
		
		print("SYSTEM COMPLETED!")
		
except Exception as err:
	failure_message = "Report generation failed!"
	
	try:
		notification_record = notification_history.create_record(
			failure_message,
		    "failure"
		)
		
		notification_history.save_record(
			notification_history_path,
		    notification_record
		)
		
	except Exception as logging_error:
		print(
			f"Notification history failed: "
			f"{logging_error}"
		)
	print("SYSTEM FAILED!")
	print(err)	