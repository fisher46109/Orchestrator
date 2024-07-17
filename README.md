# Orchestrator
## An application written in Django for remotely turning bots on and off, as well as updating them on machines. It requires an OrchestratorAgent to execute commands and send current information. 

### To install and run the Django application, follow these steps: 
1. **Clone the repository**: Download the source code from GitHub and navigate to the project directory.
2. **Create and activate a virtual environment**: Isolates the project's dependencies to avoid conflicts with other projects.
3. **Install the required packages**: Use `pip` to install all dependencies listed in the `requirements.txt` file.
```sh
pip install -r requirements.txt
```
4. **Apply database migrations**: Set up the database by creating the necessary tables and structures.
```sh
python manage.py migrate
```
**Note!** The sample repository includes a database with example data, so migrations are not necessary. In a production environment, the above migrations should be performed without including the database beforehand.

5. **Run the development server**: Start the local server to test the application.
```sh
python manage.py runserver
```
6. **Open your browser**: Access the application through a web browser.

      [http://127.0.0.1:8000](http://127.0.0.1:8000)
      or
      [http://localhost:8000](http://localhost:8000)

### Communication with the agent occurs by querying and setting values in the orchestrator's API by the Agent at specified intervals. Each Agent queries the API using its own machine name and user, and reads control data for itself. The Agent can read a request for:
- Start Bot
- Stop Bot (with safe shutdown within a specified place in code (need implementation agent_handler.py in bot code))
- Kill Bot
- Update Bot code with zip file
