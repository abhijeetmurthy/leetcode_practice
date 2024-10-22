import json

class Config:
    def __init__(self, config_path='config.json'):
        with open(config_path, 'r') as file:
            config = json.load(file)
        self.github_username = config['github_username']
        self.github_token = config['github_token']
        self.leetcode_username = config['leetcode_username']
        self.leetcode_password = config['leetcode_password']
        self.github_repo = config['github_repo']
