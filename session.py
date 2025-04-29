import time 
import json 
import os

class Session:
    def __init__(self) -> None:
        self.session_file = 'session.dat'
        self.session_timeout = 10 # В сек
        self.session_data = self.load_session()

    def load_session(self):
        if os.path.exists(self.session_file):
            try:
                with open(self.session_file, "r") as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def create_session(self):
        self.session_data = {
            "auth_time": time.time(),
            "active": True
        }
        self.save_session()

    def check_session(self):
        if not self.session_data.get('active'):
            return False
        
        if time.time() - self.session_data['auth_time'] > self.session_timeout:
            self.clear_session()
            return False
    
        return True

    def save_session(self):
        with open(self.session_file, 'w') as f:
            json.dump(self.session_data, f)
    
    def clear_session(self):
        self.session_data = {}
        if os.path.exists(self.session_file):
            os.remove(self.session_file)

session = Session()
