# README

## Flask Application with /htop Endpoint

This repository contains the Python code for a Flask application that serves system information and process details at the /htop endpoint. The application is designed to display the following information:
- *Name* 
- *Username* 
- *Server Time:* Current server time in IST
- *Top Output:* A snapshot of the system's running processes, similar to the Linux top command.

---

## Features
1. *Dynamic System Information*: Displays live system data such as process details, CPU usage, memory usage, and more.
2. *Flask Framework*: Lightweight and easy-to-deploy Python web framework.
3. *Public Endpoint*: Designed to be accessible via a public port for testing and demonstration purposes.

---

## Usage Instructions
1. Clone the repository:
   bash
   git clone https://github.com/Deepanshu21coder/Morphle-Lab.git
   
2. Navigate to the project directory:
   
   cd Morphle-Lab
   
3. Install dependencies:

   pip install flask
   pip install pytz
   
5. Run the application:
   
   python app.py
   
5. Access the application in your browser at:
   
   http://localhost:5000/htop
   

---

## Note on Deployment

Due to a network error in GitHub Codespaces, we were unable to deploy and test the application in a live environment. As a result, this repository only contains the Python code for the application. If you encounter issues replicating the environment or running the code, please ensure that:
- You have Python 3.x installed.
- The necessary dependencies are installed (flask).
- Your local or cloud environment supports running Flask applications.

---

## Example Output

### Expected Output in Browser:
The /htop endpoint will display output similar to this:


Name: Deepanshu  
User: codespace  
Server Time (IST): 2025-02-18 17:07:27  
TOP output:  
<Linux top command output>


For more details, refer to the app.py file in this repository.

---

## Limitations
1. The live Codespaces deployment is currently unavailable due to network issues.
2. Testing was conducted locally; differences may arise when deployed on other environments.

---
