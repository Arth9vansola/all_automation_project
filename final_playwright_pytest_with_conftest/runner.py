import unittest
import HtmlTestRunner
import os

if __name__ == "__main__":

    os.makedirs("reports", exist_ok=True)

    # Discover ALL test files inside Tests folder
    suite = unittest.TestLoader().discover(
        start_dir="Tests",        # main test directory
        pattern="test_*.py",      # naming convention
        top_level_dir="."        # project root
    )

    runner = HtmlTestRunner.HTMLTestRunner(
        output="reports",
        report_name="Merged_report_playwright_very_final",
        report_title="Automation Exercise + Sauce Demo Test Report",
        combine_reports=True,
        descriptions=True,
        verbosity=2
    )

    runner.run(suite)