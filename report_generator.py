# ============================================================              
#                 Report Generator
# ============================================================

import os
from datetime import datetime


def save_report(student_name, report):
    """
    Save the final AI mock interview report
    into the reports folder.
    """

    # Create reports folder if it does not exist
    reports_folder = "reports"
    os.makedirs(reports_folder, exist_ok=True)

    # Create a safe filename
    safe_name = student_name.strip().replace(" ", "_")

    # Add date and time to filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{safe_name}_Interview_Report_{timestamp}.txt"

    # Complete file path
    filepath = os.path.join(reports_folder, filename)

    try:
        # Save report
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(report)

        print("\n================================================")
        print("Interview Report Saved Successfully")
        print("================================================")
        print("Report File :", filepath)

        return filepath

    except Exception as e:

        print("\nError while saving interview report.")
        print("Error :", e)

        return None