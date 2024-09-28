import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ApiClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get_users():
        """
        Fetch all users from the /users API.
        """
        url = f"{ApiClient.BASE_URL}/users"
        logger.info(f"Fetching users from {url}")
        response = requests.get(url)
        response.raise_for_status()
        users = response.json()
        logger.info(f"Fetched {len(users)} users successfully.")
        return users

    @staticmethod
    def get_todos(user_id):
        """
        Fetch todos for a given user from the /todos API.
        
        Args:
            user_id (int): The ID of the user for whom todos are being fetched.

        Returns:
            List of todos for the user.
        """
        url = f"{ApiClient.BASE_URL}/todos"
        logger.info(f"Fetching todos for user_id {user_id} from {url}")
        response = requests.get(url, params={'userId': user_id})
        response.raise_for_status()
        todos = response.json()
        logger.info(f"Fetched {len(todos)} todos for user_id {user_id}.")
        return todos
