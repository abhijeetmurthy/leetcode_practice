import requests

class LeetCodeService:
    def __init__(self, config):
        self.leetcode_base_url = 'https://leetcode.com'
        self.api_url = f'{self.leetcode_base_url}/api/submissions/{config.leetcode_username}'
        self.config = config
        self.session = requests.Session()
    
    def login(self):
        payload = {
            'login': self.config.leetcode_username,
            'password': self.config.leetcode_password
        }
        response = self.session.post(f'{self.leetcode_base_url}/accounts/login/', data=payload)
        if response.status_code == 200:
            print("Logged into LeetCode successfully.")
        else:
            raise Exception("Failed to log into LeetCode.")
    
    def fetch_submissions(self):
        response = self.session.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error fetching LeetCode submissions.")
