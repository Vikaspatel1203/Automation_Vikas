import logging, pytest
from main_test.Report_Mail import *
# from NEW.constants import SERVICE_LOGS_DIR

# from NEW.utils import ServiceHelper

ENV = "QA"
def pytest_configure(config):
    logging.info("In Configure")
def pytest_unconfigure(config):
    print(("7777777777777777"))
    fetch()
    # TestReport_Generation()
    # Summary_Table_Formation()
    # Send_Mail()
    # read_file()
    logging.info("finally")


# @pytest.fixture(scope="session", autouse=True)
# def services():
#     """
#     Test helper fixture provides APIs to interface with all services in the test infrastructure.
#     """
#     # Initialize a Services instance.
#     all_services = ServiceHelper()

#     # Startup all the services defined in the "test" docker compose file and wait for services to be
#     # ready for testing.
#     try:
#         all_services.start_up()
#     except Exception:
#         pytest.exit(
#             "Stopping the execution of tests due to the services failing to start."
#         )

#     yield all_services
# #
# #     # Only tear down all the services if NOT in developer mode. Typicially, when a developer has
# #     # bashed into the test runner container who is manually running tests, the preference is to keep
# #     # the containers up and running allowing ease of test execution without having to wait for
# #     # containers to spin up each time.
# #     # if os.environ.get("DEV_MODE", "False") == "False":
# #     #     # Save the restserver API log to disk.
# #     #     if not os.path.exists(SERVICE_LOGS_DIR):
# #     #         os.makedirs(SERVICE_LOGS_DIR)
# #     #     all_services.save_logs()
# #     #
# #     #     # Shutdown all services.
# #     #     all_services.tear_down()
# #     #
# #     #     self.driver = driver
