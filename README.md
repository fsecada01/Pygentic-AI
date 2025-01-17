<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="readmeai/assets/logos/purple.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# PYGENTIC-AI

<em>Empowering AI innovation with seamless asynchronous processing.</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/fsecada01/Pygentic-AI?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/fsecada01/Pygentic-AI?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/fsecada01/Pygentic-AI?style=default&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/fsecada01/Pygentic-AI?style=default&color=0080ff" alt="repo-language-count">

<!-- default option, no dependency badges. -->


<!-- default option, no dependency badges. -->

</div>
<br>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

Pygentic-AI simplifies project setup and backend operations for developers.

**Why Pygentic-AI?**

This project automates Python environment setup and dependency management, ensuring a smooth development workflow. The custom logger enhances backend logging efficiency, while the RESTful API server streamlines backend operations.

- **🚀 Automated Python Setup:** Simplify environment configuration and dependency management.
- **💡 Custom Logger:** Efficient logging with customizable features for backend operations.
- **🌐 RESTful API Server:** Facilitate seamless backend operations with a robust API server.

---

## Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Follows a modular architecture with clear separation of concerns</li><li>Utilizes FastAPI for building APIs</li><li>Integrates with SQLAlchemy for database operations</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Consistent code style following PEP8 guidelines</li><li>Includes type hints for improved code readability and maintainability</li><li>Uses logging extensively for debugging and monitoring</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive documentation using Sphinx and reStructuredText</li><li>Includes detailed API documentation using Swagger UI</li><li>README.md provides clear setup and usage instructions</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with Celery for asynchronous task processing</li><li>Utilizes Pydantic for data validation and parsing</li><li>Includes integration with OpenTelemetry for observability</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Organized into reusable modules for easy maintenance and extensibility</li><li>Follows the SOLID principles for better code structure</li><li>Uses dependency injection for decoupling components</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes unit tests for critical components using pytest</li><li>Utilizes test fixtures for reusable test setup</li><li>Implements continuous integration with GitHub Actions for automated testing</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimizes database queries using SQLAlchemy ORM</li><li>Utilizes async features for improved concurrency</li><li>Includes caching mechanisms for faster data retrieval</li></ul> |
| 🛡️ | **Security**      | <ul><li>Follows best practices for handling user authentication and authorization</li><li>Implements input validation to prevent common security vulnerabilities</li><li>Includes security headers and encryption for data protection</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Uses a wide range of dependencies for various functionalities</li><li>Manages dependencies using pip and uv for locking versions</li><li>Includes detailed dependency files for easy reproducibility</li></ul> |

---

## Project Structure

```sh
└── Pygentic-AI/
    ├── bin
    │   ├── build.sh
    │   ├── linux_build.sh
    │   ├── python_build.sh
    │   └── start.sh
    ├── compose.yaml
    ├── core_requirements.in
    ├── core_requirements.txt
    ├── dev_requirements.in
    ├── dev_requirements.txt
    ├── docker
    │   ├── celery
    │   └── ranked_jobs_ms
    ├── Dockerfile
    ├── pyproject.toml
    ├── README.md
    ├── src
    │   ├── app.py
    │   ├── backend
    │   └── cworker.py
    └── uv.lock
```

### Project Index

<details open>
	<summary><b><code>PYGENTIC-AI/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/compose.yaml'>compose.yaml</a></b></td>
					<td style='padding: 8px;'>- Define services and configurations for web and celery_service containers, including image, resources, ports, environment variables, volumes, labels, health checks, and network settings<br>- Services are deployed with specific memory limits and exposed ports, with web service catering to production and celery_service to staging environments<br>- Traefik is utilized for routing and SSL termination.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/core_requirements.in'>core_requirements.in</a></b></td>
					<td style='padding: 8px;'>Define project dependencies and requirements using the core_requirements.in file to ensure seamless integration and functionality across the codebase architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/core_requirements.txt'>core_requirements.txt</a></b></td>
					<td style='padding: 8px;'>Generates a compiled list of core requirements for the project, ensuring all necessary dependencies are included for seamless functionality across various modules and components.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/dev_requirements.in'>dev_requirements.in</a></b></td>
					<td style='padding: 8px;'>- Enhance development environment by managing dependencies efficiently with dev_requirements.in<br>- This file specifies essential tools like Alembic, Black, and Pre-commit to streamline the development process<br>- Optimize code formatting and debugging with JupyterLab extensions, ensuring a robust and efficient workflow.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/dev_requirements.txt'>dev_requirements.txt</a></b></td>
					<td style='padding: 8px;'>- Generate a list of development requirements for the project, outlining dependencies and their versions<br>- The file was auto-generated using uv to compile the dev_requirements.in file<br>- It includes various packages required for development, such as alembic, fastapi, and jupyter-server<br>- Each dependency is specified with its version number for accurate package management.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/Dockerfile'>Dockerfile</a></b></td>
					<td style='padding: 8px;'>- Create a Docker image for Pygentic-AI project, setting up necessary environment variables, cloning the project repository, and configuring the workspace<br>- Install dependencies, create user celery, set up directories, and make scripts executable<br>- Finally, build and start the Python application within the designated workspace.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
					<td style='padding: 8px;'>- Define linting rules and file exclusions for the project structure in the pyproject.toml file<br>- Ensure code quality by enforcing specific linting standards, excluding unnecessary directories, and setting line length limits<br>- This configuration enhances code readability and maintainability across the codebase.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- bin Submodule -->
	<details>
		<summary><b>bin</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ bin</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/bin\build.sh'>build.sh</a></b></td>
					<td style='padding: 8px;'>Update and install project dependencies using the provided build script.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/bin\linux_build.sh'>linux_build.sh</a></b></td>
					<td style='padding: 8px;'>- Set up a Linux environment for the project by installing essential dependencies and tools<br>- Ensure a smooth development experience by preparing the system with required packages like build tools, Python 3.13, PostgreSQL, and more<br>- This script streamlines the initial setup process, enabling developers to focus on building the project without worrying about environment configuration.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/bin\python_build.sh'>python_build.sh</a></b></td>
					<td style='padding: 8px;'>- Automates Python environment setup and dependency management for the project<br>- Creates a virtual environment, installs necessary packages, and syncs core and development requirements using pip-tools<br>- Facilitates streamlined development workflow by ensuring consistent package versions across environments.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/bin\start.sh'>start.sh</a></b></td>
					<td style='padding: 8px;'>- Launches the application using Gunicorn with specified configurations, such as the number of workers, timeout, and port<br>- The script activates the virtual environment and starts the server to handle incoming requests.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- src Submodule -->
	<details>
		<summary><b>src</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ src</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\app.py'>app.py</a></b></td>
					<td style='padding: 8px;'>- Define exception handlers and mount static files for the FastAPI app using the provided code<br>- Handle validation errors and custom exceptions, logging details and returning appropriate responses<br>- Serve static files from the specified directory for the frontend.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\cworker.py'>cworker.py</a></b></td>
					<td style='padding: 8px;'>- Improve concurrency by managing worker threads efficiently<br>- This code file in src\cworker.py orchestrates thread creation and execution within the projects architecture.</td>
				</tr>
			</table>
			<!-- backend Submodule -->
			<details>
				<summary><b>backend</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ src.backend</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\logger.py'>logger.py</a></b></td>
							<td style='padding: 8px;'>- Implement a custom logger using Loguru for efficient logging in the backend<br>- The logger supports various log levels and customization options, enhancing the logging experience<br>- It includes features like log rotation, retention, and different log formats<br>- The code ensures robust logging functionality for the project.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\utils.py'>utils.py</a></b></td>
							<td style='padding: 8px;'>- Define utility functions to retrieve database URLs based on environment and fetch values from environment variables or configuration files<br>- The <code>get_db_url</code> function constructs a database URL for different environments, while <code>get_val</code> retrieves values with fallback options<br>- These functions enhance flexibility and maintainability in managing configurations and environment variables.</td>
						</tr>
					</table>
					<!-- core Submodule -->
					<details>
						<summary><b>core</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ src.backend.core</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\core\consts.py'>consts.py</a></b></td>
									<td style='padding: 8px;'>- Define the AI_MODEL and default_system_prompt for the GPT-4o AI assistant in the consts.py file<br>- The AI_MODEL specifies the model used, while the default_system_prompt outlines the AIs function of generating SWOT analyses.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\core\core.py'>core.py</a></b></td>
									<td style='padding: 8px;'>- Define a SQLModel and Agent Dependencies for SWOT Analysis, creating a SwotAgent with specified parameters for AI model, system prompt, and retries<br>- This code file in the core module plays a crucial role in structuring and managing SWOT analysis responses within the projects architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\core\main.py'>main.py</a></b></td>
									<td style='padding: 8px;'>Implement core functionality for backend services in the main.py file.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\core\tools.py'>tools.py</a></b></td>
									<td style='padding: 8px;'>- Describe how the <code>tools.py</code> file in <code>src\backend\core</code> facilitates fetching website content, analyzing competition using the Gemini model, and obtaining insights from Reddit<br>- The functions within this file leverage various libraries and APIs to perform these tasks efficiently.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\core\utils.py'>utils.py</a></b></td>
									<td style='padding: 8px;'>- Define a function to report tool usage and results within the projects core architecture<br>- The function checks and updates tool usage history, notifying an update function if available<br>- This contributes to tracking tool usage and ensuring status updates are communicated effectively.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- db Submodule -->
					<details>
						<summary><b>db</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ src.backend.db</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\db\base.py'>base.py</a></b></td>
									<td style='padding: 8px;'>- Generate base SQLModel class for project, addressing Pydantic V2.5 issue with <code>__pydantic_extra__</code> attribute<br>- Inherits from SQLModel and sets necessary attributes<br>- Integrated with project metadata and configured for eager defaults.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\db\consts.py'>consts.py</a></b></td>
									<td style='padding: 8px;'>Define database constants for backend operations in the project structure.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\db\core.py'>core.py</a></b></td>
									<td style='padding: 8px;'>Manage core database operations for the backend system, ensuring efficient data handling and storage.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\db\db.py'>db.py</a></b></td>
									<td style='padding: 8px;'>- Create and manage async SQLA sessions, handle database operations, and ensure database schema creation<br>- Includes functions for checking database existence, creating databases, and setting the current schema<br>- Provides utilities for creating database engines and managing database connections<br>- Mainly focuses on database setup and interaction for the project.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\db\main.py'>main.py</a></b></td>
									<td style='padding: 8px;'>Implement database connection and query functions to manage data persistence for the backend services.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\db\utils.py'>utils.py</a></b></td>
									<td style='padding: 8px;'>- Enhances database operations by providing utility functions<br>- Facilitates seamless interaction with the database layer.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- server Submodule -->
					<details>
						<summary><b>server</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ src.backend.server</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\server\consts.py'>consts.py</a></b></td>
									<td style='padding: 8px;'>Define and store constant values used throughout the backend server architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\server\core.py'>core.py</a></b></td>
									<td style='padding: 8px;'>Implement core server functionality to handle incoming requests and manage data operations within the backend architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\server\main.py'>main.py</a></b></td>
									<td style='padding: 8px;'>- Implement a RESTful API server in Python to handle backend operations for the project<br>- The main.py file serves as the entry point for the server, orchestrating requests and responses<br>- It plays a crucial role in managing the communication between the frontend and backend components of the application.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\server\router.py'>router.py</a></b></td>
									<td style='padding: 8px;'>Define API routes and request handling logic for the backend server.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\server\utils.py'>utils.py</a></b></td>
									<td style='padding: 8px;'>- Enhances server functionality by providing utility functions<br>- Improves codebase architecture by centralizing common operations<br>- Facilitates streamlined development and maintenance processes<br>- Promotes code reusability and efficiency within the backend server module.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- settings Submodule -->
					<details>
						<summary><b>settings</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ src.backend.settings</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\settings\backend_options.py'>backend_options.py</a></b></td>
									<td style='padding: 8px;'>- Generate SQL database connection URLs based on provided configurations for different environments using accepted dialects, including PostgreSQL and SQLite<br>- Import these configurations into the appropriate settings file to integrate with the Django Database settings.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\settings\base.py'>base.py</a></b></td>
									<td style='padding: 8px;'>Define project settings including backend and frontend directories, database URL, and debug mode in the base settings file.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\settings\consts.py'>consts.py</a></b></td>
									<td style='padding: 8px;'>Define database dialects and set secret key for project configuration.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\settings\core.py'>core.py</a></b></td>
									<td style='padding: 8px;'>- Enhances core settings functionality by providing centralized configuration management<br>- Facilitates seamless access and modification of key system parameters<br>- Improves maintainability and scalability of the project by consolidating settings logic.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\settings\dev.py'>dev.py</a></b></td>
									<td style='padding: 8px;'>Define development settings for backend with local database configuration and debugging enabled.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\settings\main.py'>main.py</a></b></td>
									<td style='padding: 8px;'>- Enhances backend settings functionality by managing configurations efficiently<br>- Facilitates seamless customization and optimization of settings across the codebase architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\settings\prod.py'>prod.py</a></b></td>
									<td style='padding: 8px;'>- Define production settings for the backend, including database configuration and debugging options<br>- Extends base settings to inherit common configurations<br>- Centralizes cloud database settings for easy management and maintenance.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\settings\utils.py'>utils.py</a></b></td>
									<td style='padding: 8px;'>- Enhance backend settings functionality by providing utility functions for the codebase architecture<br>- The <code>utils.py</code> file in the <code>src\backend\settings</code> directory plays a crucial role in enabling streamlined operations and improved performance within the project structure.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- site Submodule -->
					<details>
						<summary><b>site</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ src.backend.site</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\site\consts.py'>consts.py</a></b></td>
									<td style='padding: 8px;'>- Define constants and data structures for tracking analysis progress and results in the backend of the site architecture<br>- Includes messages for analysis status, sets for running tasks, and dictionaries for storing status and results.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\site\core.py'>core.py</a></b></td>
									<td style='padding: 8px;'>Implement core functionality for the site backend, facilitating key operations within the project architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\site\main.py'>main.py</a></b></td>
									<td style='padding: 8px;'>Improve site performance by caching API responses in the main.py file.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\site\router.py'>router.py</a></b></td>
									<td style='padding: 8px;'>- Implement a backend API router for a SWOT analysis tool<br>- The router handles URL analysis requests, updates status messages, and provides analysis results<br>- It manages session IDs, progress tracking, and result storage<br>- The code integrates with FastAPI, Starlette, and Jinja2 for web functionality.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\site\utils.py'>utils.py</a></b></td>
									<td style='padding: 8px;'>- Enhances backend functionality by providing utility functions for the site<br>- This code file in the backend architecture aids in streamlining operations and improving overall performance.</td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- docker Submodule -->
	<details>
		<summary><b>docker</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ docker</b></code>
			<!-- celery Submodule -->
			<details>
				<summary><b>celery</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ docker.celery</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/docker\celery\start.sh'>start.sh</a></b></td>
							<td style='padding: 8px;'>- Initiates and manages Celery workers, beat scheduler, and Flower for the projects asynchronous task processing<br>- Handles worker availability checks and starts necessary services within the specified project directory.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- ranked_jobs_ms Submodule -->
			<details>
				<summary><b>ranked_jobs_ms</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ docker.ranked_jobs_ms</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/docker\ranked_jobs_ms\build.sh'>build.sh</a></b></td>
							<td style='padding: 8px;'>- Install necessary dependencies for the ranked jobs microservice in the Docker container<br>- The script sets up essential tools like Python, PostgreSQL, and Git, ensuring a robust environment for the microservice to run smoothly.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/docker\ranked_jobs_ms\python_build.sh'>python_build.sh</a></b></td>
							<td style='padding: 8px;'>- Automates Python environment setup and dependency management for the ranked jobs microservice in the Docker architecture<br>- Sets up virtual environment, compiles requirements, and syncs dependencies for smooth execution.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/docker\ranked_jobs_ms\python_start.sh'>python_start.sh</a></b></td>
							<td style='padding: 8px;'>- Launches the Python application using Gunicorn with specified configurations like the number of workers, timeout, and port<br>- The script activates the virtual environment and starts the server to handle incoming requests.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip, Uv
- **Container Runtime:** Docker

### Installation

Build Pygentic-AI from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/fsecada01/Pygentic-AI
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd Pygentic-AI
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![docker][docker-shield]][docker-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [docker-shield]: https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white -->
	<!-- [docker-link]: https://www.docker.com/ -->

	**Using [docker](https://www.docker.com/):**

	```sh
	❯ docker build -t fsecada01/Pygentic-AI .
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pip][pip-shield]][pip-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
	<!-- [pip-link]: https://pypi.org/project/pip/ -->

	**Using [pip](https://pypi.org/project/pip/):**

	```sh
	❯ pip install -r core_requirements.in, core_requirements.txt, dev_requirements.in, dev_requirements.txt
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![uv][uv-shield]][uv-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [uv-shield]: https://img.shields.io/badge/uv-DE5FE9.svg?style=for-the-badge&logo=uv&logoColor=white -->
	<!-- [uv-link]: https://docs.astral.sh/uv/ -->

	**Using [uv](https://docs.astral.sh/uv/):**

	```sh
	❯ uv sync --all-extras --dev
	```

### Usage

Run the project with:

**Using [docker](https://www.docker.com/):**
```sh
docker run -it {image_name}
```
**Using [pip](https://pypi.org/project/pip/):**
```sh
python {entrypoint}
```
**Using [uv](https://docs.astral.sh/uv/):**
```sh
uv run python {entrypoint}
```

### Testing

Pygentic-ai uses the {__test_framework__} test framework. Run the test suite with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
pytest
```
**Using [uv](https://docs.astral.sh/uv/):**
```sh
uv run pytest tests/
```

---

## Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## Contributing

- **💬 [Join the Discussions](https://github.com/fsecada01/Pygentic-AI/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/fsecada01/Pygentic-AI/issues)**: Submit bugs found or log feature requests for the `Pygentic-AI` project.
- **💡 [Submit Pull Requests](https://github.com/fsecada01/Pygentic-AI/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/fsecada01/Pygentic-AI
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/fsecada01/Pygentic-AI/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=fsecada01/Pygentic-AI">
   </a>
</p>
</details>

---

## License

Pygentic-ai is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---
