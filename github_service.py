import subprocess

class GitHubService:
    def __init__(self, config):
        self.config = config
        self.repo_name = config.github_repo
    
    def push_to_github(self, filename):
        subprocess.run(['git', 'add', filename])
        subprocess.run(['git', 'commit', '-m', f'Add {filename} solution'])
        subprocess.run(['git', 'push'])
    
    def save_to_file(self, title, code):
        filename = f"{title.replace(' ', '_').replace('-', '_')}.py"
        with open(filename, 'w') as file:
            file.write(code)
        return filename
