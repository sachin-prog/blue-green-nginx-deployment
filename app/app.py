from flask import Flask
import os
app = Flask(__name__)

VERSION = os.getenv("App_version", "unknown")
ENVIRONMENT = os.getenv("App_environment", "unknown")

@app.route('/')
def home():
    return f"""
    <html>
        <head>
            <title>Blue Green Deployment Project</title>
        </head>
        <body>
            <h1>Blue-Green Deployment Demo</h1>
            <h2>Application Version: {VERSION}</h2>
            <h3>Environment: {ENVIRONMENT}</h3>
            <p>Welcome to the Blue-Green Deployment Demo application! This application is designed to showcase the principles of blue-green deployment, a technique used to reduce downtime and risk during software releases.</p>
            <p>In a blue-green deployment, two identical environments (blue and green) are maintained. One environment (e.g., blue) serves live production traffic, while the other (e.g., green) is idle. When a new version of the application is ready, it is deployed
            <p> Deployment Successful! The new version is now live and serving traffic.</p>
        </body>
    </html>
    """
@app.route('/health')
def health():  
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

    