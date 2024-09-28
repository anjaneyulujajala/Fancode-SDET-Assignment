import logging

# Set up logging
logger = logging.getLogger(__name__)

class UserService:
    @staticmethod
    def filter_users_in_fancode_city(users):
        """
        Filters users who belong to the 'FanCode' city.
        FanCode city is defined by latitude between -40 to 5 and longitude between 5 to 100.
        
        Args:
            users (list): List of user objects.

        Returns:
            List of users in FanCode city.
        """
        logger.info(f"Filtering users from the FanCode city...")
        fancode_users = []
        for user in users:
            lat = float(user['address']['geo']['lat'])
            lng = float(user['address']['geo']['lng'])
            if -40 <= lat <= 5 and 5 <= lng <= 100:
                fancode_users.append(user)
                logger.info(f"User {user['id']} is in the FanCode city.")
        logger.info(f"Found {len(fancode_users)} users in FanCode city.")
        return fancode_users

    @staticmethod
    def calculate_completion_percentage(todos):
        """
        Calculates the percentage of completed tasks for a user.
        
        Args:
            todos (list): List of todos.

        Returns:
            Completion percentage (float).
        """
        total_tasks = len(todos)
        completed_tasks = sum(1 for todo in todos if todo['completed'])
        completion_percentage = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        logger.info(f"User has {completed_tasks}/{total_tasks} tasks completed ({completion_percentage}%).")
        return completion_percentage

    @staticmethod
    def check_users_task_completion(users, api_client):
        """
        Checks if all users from FanCode city have more than 50% tasks completed.
        
        Args:
            users (list): List of users.
            api_client (ApiClient): The API client to fetch todos.

        Returns:
            Dictionary with user ID as key and task completion status (True/False) as value.
        """
        logger.info(f"Checking task completion for users in FanCode city...")
        user_completion_status = {}
        for user in users:
            todos = api_client.get_todos(user['id'])
            completion_percentage = UserService.calculate_completion_percentage(todos)
            user_completion_status[user['id']] = completion_percentage > 50
            logger.info(f"User {user['id']} task completion is {completion_percentage:.2f}%. Status: {'Passed' if completion_percentage > 50 else 'Failed'}.")
        return user_completion_status
