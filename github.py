import git
import os
import shutil

class Github():
    def __init__(self,repo_url):
        self.repo_url = repo_url
        
    def check_remote_repo(self):
        """Deze funcite zal de repo controleren of er een config file beschickbaar is zoja return yes """
        try:
            local_directory = "temp_directory"
            repo = git.Repo.clone_from(self.repo_url, local_directory)
            response = None
            config_file_path = os.path.join(local_directory, "config", "config.txt")
            if os.path.exists(config_file_path):
                with open(config_file_path, "r") as file:
                    response = file.read()
            repo.close()
            shutil.rmtree(local_directory)
            if response:
                return True
            else:
                return False
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False

    def get_config(self):
        pass

    def load_modules(self):
        pass

    def send_logs_to_github(self,id):
        """Deze functie zal de inhoud van de map logs kopieren naar temp_dir en vervolgens de log files gaan versturen naar github """
        try:
            local_directory = "temp_directory"
            repo = git.Repo.clone_from(self.repo_url, local_directory)
            logs_directory = os.path.join(local_directory, "logs" , id)
            shutil.copytree('logs', logs_directory)
            repo.git.add(all=True)
            repo.index.commit("Add new log entries")
            origin = repo.remote(name="origin")
            origin.push()
            repo.close()
            shutil.rmtree(local_directory)
            return True
        except (git.exc.GitCommandError, FileNotFoundError):
            return False