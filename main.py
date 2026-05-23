# THE ORCHESTRATION STAGE.
import json
from pathlib import Path

from core.report_builder import ReportBuilder
from core.notifier import Notifier
from core.report_storage import ReportStorage


analytics_path = Path("sample_data/analytic_summary.json")
report_path = Path("reports/usage_report.txt")

report_builder = ReportBuilder()
notifier = Notifier()
report_storage = ReportStorage()

try:
	with open(analytics_path, "r") as file:
		analytics_data = json.load(file)
		
		report_text = report_builder.build_report(analytics_data)
		
		saved_path = report_storage.save_report(report_path, report_text)
		
		notifier.notify("Report generated successfully")
		
		print("\n=== FINAL SUMMARY ===")
		
		print("Report saved to:", saved_path)
		
		print("Notification status: SENT")
		
		print("SYSTEM COMPLETED!")
		
except Exception as err:
	print("SYSTEM FAILED!")
	print(err)