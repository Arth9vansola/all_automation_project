# # import unittest
# # import HtmlTestRunner
# # import os

# # if __name__ == "__main__":

# #     os.makedirs("reports", exist_ok=True)

# #     suite = unittest.TestLoader().discover(
# #         start_dir="Tests",      # your test folder
# #         pattern="test_*.py"     # naming convention
# #     )


# #     runner = HtmlTestRunner.HTMLTestRunner(
# #         output="reports",
# #         report_name="AutomationReport",
# #         report_title="Automation Exercise Test Report",
# #         combine_reports=True,
# #         descriptions=True,
# #         verbosity=2
# #     )

# #     runner.run(suite)


# import os
# import unittest

# import HtmlTestRunner
# from HtmlTestRunner.result import (
#     HtmlTestResult,
#     _SubTestInfos,
#     render_html,
#     strip_module_names,
# )


# class GroupedHtmlTestResult(HtmlTestResult):
#     def _get_info_by_testcase(self):
#         """Group test results by package (e.g., Tests.Automation_Exercise)."""
#         tests_by_group = {}

#         subtest_names = set(self.subtests.keys())
#         for test_name, subtests in self.subtests.items():
#             subtest_info = _SubTestInfos(test_name, subtests)
#             group_name = self._group_name_from_id(test_name)
#             tests_by_group.setdefault(group_name, []).append(subtest_info)

#         for tests in (self.successes, self.failures, self.errors, self.skipped):
#             for test_info in tests:
#                 if test_info.is_subtest or test_info.test_id in subtest_names:
#                     continue
#                 if isinstance(test_info, tuple):
#                     test_info = test_info[0]
#                 group_name = self._group_name_from_id(test_info.test_id)
#                 tests_by_group.setdefault(group_name, []).append(test_info)

#         for group in tests_by_group.values():
#             group.sort(key=lambda x: x.test_id)

#         return tests_by_group

#     @staticmethod
#     def _group_name_from_id(test_id):
#         parts = test_id.split(".")
#         if len(parts) >= 2:
#             return ".".join(parts[:2])
#         return ".".join(parts[:-1]) if len(parts) > 1 else test_id

#     def _regroup_results(self, all_results):
#         grouped = {}
#         for tests in all_results.values():
#             for test_info in tests:
#                 group_name = self._group_name_from_id(test_info.test_id)
#                 grouped.setdefault(group_name, []).append(test_info)

#         for group in grouped.values():
#             group.sort(key=lambda x: x.test_id)

#         return grouped

#     def generate_reports(self, testRunner):
#         """Generate report(s) grouped by package name."""
#         status_tags = ("success", "danger", "warning", "info")
#         all_results = self._get_info_by_testcase()
#         all_results = self._regroup_results(all_results)
#         summaries = self._get_report_summaries(all_results, testRunner)

#         if not testRunner.combine_reports:
#             for test_case_class_name, test_case_tests in all_results.items():
#                 header_info = self._get_header_info(test_case_tests, testRunner.start_time)
#                 html_file = render_html(
#                     testRunner.template,
#                     title=testRunner.report_title,
#                     header_info=header_info,
#                     all_results={test_case_class_name: test_case_tests},
#                     status_tags=status_tags,
#                     summaries=summaries,
#                     **testRunner.template_args,
#                 )
#                 if testRunner.report_name is None:
#                     report_name_body = self.default_prefix + test_case_class_name
#                 else:
#                     report_name_body = "{}_{}".format(testRunner.report_name, test_case_class_name)
#                 self.generate_file(testRunner, report_name_body, html_file)
#         else:
#             header_info = self._get_header_info(
#                 [item for sublist in all_results.values() for item in sublist],
#                 testRunner.start_time,
#             )
#             html_file = render_html(
#                 testRunner.template,
#                 title=testRunner.report_title,
#                 header_info=header_info,
#                 all_results=all_results,
#                 status_tags=status_tags,
#                 summaries=summaries,
#                 **testRunner.template_args,
#             )
#             if testRunner.report_name is not None:
#                 report_name_body = testRunner.report_name
#             else:
#                 report_name_body = self.default_prefix + "_".join(strip_module_names(list(all_results.keys())))
#             self.generate_file(testRunner, report_name_body, html_file)

# if __name__ == "__main__":

#     os.makedirs("reports", exist_ok=True)

#     # Discover tests per site so the report shows two sections
#     automation_suite = unittest.TestLoader().discover(
#         start_dir=os.path.join("Tests", "Automation_Exercise"),
#         pattern="test_*.py",
#         top_level_dir="."
#     )
#     sauce_suite = unittest.TestLoader().discover(
#         start_dir=os.path.join("Tests", "Sauce_demo_site"),
#         pattern="test_*.py",
#         top_level_dir="."
#     )


#     suite = unittest.TestSuite([automation_suite, sauce_suite])
#     print(suite)
#     runner = HtmlTestRunner.HTMLTestRunner(
#         output="reports",
#         report_name="merged_html_report",
#         report_title="Automation Exercise + Sauce Demo Test Report",
#         combine_reports=True,
#         descriptions=True,
#         add_timestamp=True,
#         verbosity=2,
#         resultclass=GroupedHtmlTestResult
#     )

#     runner.run(suite)



# # import unittest
# # import HtmlTestRunner
# # import os

# # if __name__ == "__main__":

# #     os.makedirs("reports", exist_ok=True)

# #     suite = unittest.TestLoader().discover(
# #         start_dir="Tests",      # your test folder
# #         pattern="test_*.py"     # naming convention
# #     )


# #     runner = HtmlTestRunner.HTMLTestRunner(
# #         output="reports",
# #         report_name="AutomationReport",
# #         report_title="Automation Exercise Test Report",
# #         combine_reports=True,
# #         descriptions=True,
# #         verbosity=2
# #     )

# #     runner.run(suite)


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
        report_name="Merged_report_selenium_with_unittest2",
        report_title="Automation Exercise + Sauce Demo Test Report",
        combine_reports=True,
        descriptions=True,
        verbosity=2
    )

    runner.run(suite)