# Flask Video Streaming Application

This project is a simple Flask application that serves video files from a specified directory. It includes routes for rendering a main page and serving video files directly.

## Project Structure

```
flask-app
├── app.py               # Main application file with Flask setup and routes
├── requirements.txt     # Dependencies for the project
└── README.md            # Project documentation
```

## Requirements

To run this application, you need to have Python installed along with the following packages:

- Flask
- Gunicorn

## Installation

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required packages using pip:

```
pip install -r requirements.txt
```

## Running the Application

To run the application using Gunicorn, use the following command:

```
gunicorn app:app
```

This command tells Gunicorn to look for the `app` instance in the `app.py` file.

## Accessing the Application

Once the server is running, you can access the application in your web browser at:

```
http://localhost:8000
```

You can also access video files directly via:

```
http://localhost:8000/videos/<filename>
```

Replace `<filename>` with the name of the video file you wish to access.