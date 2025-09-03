import os
import importlib
import sys

# Ensure the project root is in sys.path for module imports
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Import the app module to access the Flask app and Videos directory
app_module = importlib.import_module('Kumquat.app')
app = app_module.app

def test_files_excludes_text_file():
    videos_dir = os.path.join(os.path.dirname(app_module.__file__), 'Videos')
    txt_file = os.path.join(videos_dir, 'temp_test_file.txt')

    # Create a .txt file in the Videos directory
    with open(txt_file, 'w') as f:
        f.write('temporary test file')

    client = app.test_client()
    try:
        response = client.get('/files')
        assert response.status_code == 200
        # Ensure the .txt filename is not in the response data
        assert b'temp_test_file.txt' not in response.data
    finally:
        # Clean up the test file
        if os.path.exists(txt_file):
            os.remove(txt_file)
