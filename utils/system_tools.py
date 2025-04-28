import os
import sys
import platform

class SystemTools:
    def __init__(self) -> None:
        self.platform = self.detect_platform()
        
    def open_application(self, app_name):
        pass
    
    def perform_action(self, action_type, details):
        pass
    
    def detect_platform(self):
        system = platform.system()
        # Desktop OS
        if system == "Windows":
            return "Windows"
        elif system == "Darwin":
            return "macOS"
        elif system == "Linux":
            # Further check for Android
            if "ANDROID_ARGUMENT" in os.environ:
                return "Android"
            else:
                return "Linux"
        else:
            # iOS detection (usually when running via Pythonista or similar)
            if sys.platform == "ios":
                return "iOS"
            return "Unknown"



if __name__ == "__main__":
    st = SystemTools()
    print("You are using: ", st.platform)    