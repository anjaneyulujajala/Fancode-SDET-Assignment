import pytest
import logging
from src.api_client import ApiClient
from src.user_service import UserService

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestTaskCompletion:

    @pytest.fixture(scope="module")
    def api_client(self):
        """
        Returns an instance of ApiClient.
        """
        return ApiClient()

    def test_fancode_city_users_task_completion(self, api_client):
        """
        Test case to verify that users from FanCode city have more than 50% of their tasks completed.
        """
        logger.info("Starting test: FanCode City Users Task Completion")

        users = api_client.get_users()
        fancode_users = UserService.filter_users_in_fancode_city(users)
        assert fancode_users, "No users found in FanCode city"

        user_completion_status = UserService.check_users_task_completion(fancode_users, api_client)

        for user_id, is_completed in user_completion_status.items():
            logger.info(f"Asserting user {user_id} task completion status.")
            assert is_completed, f"User with ID {user_id} has not completed more than 50% of tasks"

        logger.info("Test passed: All FanCode City users have more than 50% of their tasks completed.")
