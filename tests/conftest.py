from dotenv import load_dotenv
import os
import pytest

load_dotenv()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    current_test = os.environ.get("PYTEST_CURRENT_TEST")

    if not current_test:
        return

    test_path = current_test.split("::")[0]

    normalized_path = test_path.replace("\\", "/")

    path_parts = normalized_path.split("/")

    specs_index = path_parts.index("specs")

    feature = path_parts[specs_index + 1]
    method_folder = path_parts[specs_index + 2]

    test_file = path_parts[-1].replace(".py", "")

    log_path = os.path.join(
        "logs",
        feature,
        method_folder,
        f"log_{test_file}.txt"
    )

    if not os.path.exists(log_path):
        return

    with open(log_path, "a", encoding="utf-8") as log:

        separator = "=" * 80

        log.write(f"\nTEST STATUS: {report.outcome.upper()}\n")

        if report.failed:

            log.write("\nFAILURE MESSAGE:\n")

            log.write(f"{call.excinfo.value}\n")

            log.write("\nTRACEBACK:\n")

            log.write(f"{report.longrepr}\n")

        log.write(f"\n{separator}\n")