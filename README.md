<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="readmeai/assets/logos/purple.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# PYGENTIC-AI

<em>Empowering AI breakthroughs with Pygentic-AI innovation.</em>

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

**Pygentic-AI**

**Why Pygentic-AI?**

This project simplifies the deployment and management of AI applications. The core features include:

- **🚀 Orchestration:** Define deployment configurations with compose.yaml for seamless scalability.
- **💻 Automation:** Build Docker images effortlessly using Dockerfile for efficient environment setup.
- **🔧 Streamlined Setup:** Manage project dependencies and setup with provided build scripts.
- **🌐 Backend Functionality:** Implement essential backend features like RESTful APIs and database operations.

---

## Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Follows a modular design pattern</li><li>Utilizes microservices architecture</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Consistent coding style and formatting</li><li>Extensive unit tests coverage</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive README.md file</li><li>Inline code comments for better understanding</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integration with Docker for containerization</li><li>Uses various third-party libraries for extended functionality</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separation of concerns with clear module boundaries</li><li>Encourages code reusability through components</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes unit tests, integration tests, and possibly end-to-end tests</li><li>Continuous Integration setup for automated testing</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimized algorithms and data structures</li><li>Efficient resource utilization</li></ul> |
| 🛡️ | **Security**      | <ul><li>Follows best practices for data encryption and secure communication</li><li>Regular security audits and updates</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Uses a wide range of dependencies for various functionalities</li><li>Dependency management through pip and uv</li></ul> |

---

## Project Structure

```sh
└── Pygentic-AI/
    ├── .git
    │   └── objects
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
    ├── labs
    │   └── Untitled.ipynb
    ├── pyproject.toml
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
					<td style='padding: 8px;'>- Define services and configurations for web and celery_service containers in the compose.yaml file to orchestrate the deployment of the Pygentic AI application<br>- The file specifies resource limits, environment variables, ports, volumes, labels for Traefik routing, health checks, and network settings<br>- It ensures proper service communication and scalability within the architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/core_requirements.in'>core_requirements.in</a></b></td>
					<td style='padding: 8px;'>- Generate a list of essential Python packages required for the projects core functionality<br>- The file <code>core_requirements.in</code> specifies the dependencies necessary for running the codebase, including libraries for async operations, database connectivity, API development, task queuing, and more.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/core_requirements.txt'>core_requirements.txt</a></b></td>
					<td style='padding: 8px;'>- Generate a list of core project dependencies and their versions<br>- The list is automatically created by uv using the command uv pip compile--strip-extras core_requirements.in-o core_requirements.txt<br>- The file core_requirements.txt contains essential libraries like aiofiles, aiomysql, amqp, and more, necessary for the project's functionality.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/dev_requirements.in'>dev_requirements.in</a></b></td>
					<td style='padding: 8px;'>- Enhance development productivity by managing project dependencies efficiently<br>- This file specifies required packages for development, ensuring a streamlined workflow<br>- It includes tools like Alembic for database migrations, Black for code formatting, and FastAPI Debug Toolbar for debugging<br>- By defining essential dependencies, developers can maintain code quality and boost collaboration.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/dev_requirements.txt'>dev_requirements.txt</a></b></td>
					<td style='padding: 8px;'>- Generate a list of development requirements for the project by compiling dependencies specified in various configuration files<br>- The file dev_requirements.txt serves as a consolidated reference for tools and libraries essential for development tasks<br>- This compilation aids in managing and ensuring consistent development environments across the project.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/Dockerfile'>Dockerfile</a></b></td>
					<td style='padding: 8px;'>- Builds a Docker image for a Python application, setting up necessary environment variables and dependencies<br>- Clones a specific branch from a GitHub repository, configures user permissions, and prepares the environment for running the application<br>- The final image is ready to execute the Python application using predefined scripts.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
					<td style='padding: 8px;'>Define linting rules and project dependencies in pyproject.toml for the agentic_ai_service project.</td>
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
					<td style='padding: 8px;'>Update project dependencies and install required packages using the provided build script.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/bin\linux_build.sh'>linux_build.sh</a></b></td>
					<td style='padding: 8px;'>- Install necessary dependencies and tools for the project on a Linux system using the provided script<br>- The script sets up the environment by updating packages, installing essential tools, adding repositories, and configuring locales<br>- It ensures a smooth setup process for development and deployment on a Linux machine.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/bin\python_build.sh'>python_build.sh</a></b></td>
					<td style='padding: 8px;'>- Automates Python virtual environment setup and dependency management using pip-tools<br>- Sets up a virtual environment, installs necessary packages, and synchronizes dependencies for core and development requirements<br>- Facilitates streamlined project setup and maintenance.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/bin\start.sh'>start.sh</a></b></td>
					<td style='padding: 8px;'>Execute script to start the application, activating the virtual environment and launching the server with specified configurations.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- labs Submodule -->
	<details>
		<summary><b>labs</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ labs</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/labs\Untitled.ipynb'>Untitled.ipynb</a></b></td>
					<td style='padding: 8px;'>- Create necessary project directories and files if they do not exist within the specified structure<br>- This code segment ensures the presence of essential backend folders and files for the project to function correctly.</td>
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
					<td style='padding: 8px;'>Implement a RESTful API endpoint in src\app.py to handle user authentication for the project.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\cworker.py'>cworker.py</a></b></td>
					<td style='padding: 8px;'>- Implement a concurrent worker system to enhance performance and scalability<br>- This code file in src\cworker.py manages worker threads efficiently within the project structure.</td>
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
							<td style='padding: 8px;'>Capture and store application logs efficiently to enhance monitoring and debugging capabilities within the backend architecture.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\utils.py'>utils.py</a></b></td>
							<td style='padding: 8px;'>Enhances backend functionality by providing utility functions for the project.</td>
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
									<td style='padding: 8px;'>Define and centralize core constants for the backend architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\core\core.py'>core.py</a></b></td>
									<td style='padding: 8px;'>Implement core functionality for backend services, facilitating seamless communication and data processing within the project architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\core\main.py'>main.py</a></b></td>
									<td style='padding: 8px;'>- Implement core functionality for backend operations in the main.py file within the src\backend\core directory<br>- This code serves as the foundation for the entire projects backend architecture, handling essential operations and logic to ensure smooth functioning of the system.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\core\utils.py'>utils.py</a></b></td>
									<td style='padding: 8px;'>- Enhance backend functionality by providing essential utility functions<br>- This code file in the core directory plays a crucial role in supporting various backend operations<br>- It offers a collection of utility functions that streamline common tasks and enhance the overall efficiency of the backend system.</td>
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
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\db\consts.py'>consts.py</a></b></td>
									<td style='padding: 8px;'>Define database constants for backend operations in the project structure.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\db\core.py'>core.py</a></b></td>
									<td style='padding: 8px;'>Manage core database operations for the backend system, ensuring efficient data handling and storage.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\db\main.py'>main.py</a></b></td>
									<td style='padding: 8px;'>Implement database connection and query functions to manage data persistence for the backend services.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\db\utils.py'>utils.py</a></b></td>
									<td style='padding: 8px;'>- Enhances database operations by providing utility functions<br>- Facilitates efficient data management within the backend architecture.</td>
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
									<td style='padding: 8px;'>Implement server-side logic to handle API requests and responses, serving as the core backend functionality for the project.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\server\utils.py'>utils.py</a></b></td>
									<td style='padding: 8px;'>- Enhances server functionality by providing utility functions for backend operations<br>- This code file in the project architecture streamlines server-side tasks, optimizing performance and facilitating seamless data processing.</td>
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
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\settings\consts.py'>consts.py</a></b></td>
									<td style='padding: 8px;'>Define and store constant values used throughout the backend settings module.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\settings\core.py'>core.py</a></b></td>
									<td style='padding: 8px;'>- Manage core settings for the backend system, ensuring seamless configuration across modules<br>- This file serves as the central hub for defining and organizing key parameters that drive the functionality of the entire codebase<br>- It plays a crucial role in maintaining consistency and coherence in the projects architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\settings\main.py'>main.py</a></b></td>
									<td style='padding: 8px;'>- Enhances backend settings functionality by managing configuration data<br>- Facilitates dynamic adjustments to settings without code changes<br>- Improves system flexibility and scalability.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\settings\utils.py'>utils.py</a></b></td>
									<td style='padding: 8px;'>- Enhances backend functionality by providing utility functions for settings management<br>- Facilitates seamless configuration handling within the project architecture.</td>
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
									<td style='padding: 8px;'>Define and store constant values used throughout the backend site architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\site\core.py'>core.py</a></b></td>
									<td style='padding: 8px;'>Implement core functionality for the site backend, facilitating key operations within the project architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\site\main.py'>main.py</a></b></td>
									<td style='padding: 8px;'>- Implement a RESTful API endpoint for handling site data in the backend architecture<br>- This code file serves as the entry point for site-related functionalities, facilitating communication between the frontend and backend systems.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/src\backend\site\utils.py'>utils.py</a></b></td>
									<td style='padding: 8px;'>Enhance backend functionality by providing utility functions for the site.</td>
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
							<td style='padding: 8px;'>- Initiate and manage Celery workers, beat scheduler, and Flower for the projects asynchronous task processing<br>- Handles worker availability checks and starts necessary services for efficient task execution.</td>
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
							<td style='padding: 8px;'>- Install necessary dependencies for the ranked jobs microservice in the Docker container<br>- The script sets up essential tools like Python, PostgreSQL, and Git, ensuring a smooth environment for the microservice to run effectively within the architecture.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/docker\ranked_jobs_ms\python_build.sh'>python_build.sh</a></b></td>
							<td style='padding: 8px;'>Generate and synchronize Python virtual environment and dependencies for ranked jobs microservice using UV.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/fsecada01/Pygentic-AI/blob/master/docker\ranked_jobs_ms\python_start.sh'>python_start.sh</a></b></td>
							<td style='padding: 8px;'>- Launches the Python application using Gunicorn with specified configurations for workers, timeouts, and ports<br>- The script activates the virtual environment and starts the server, ensuring optimal performance and accessibility for the ranked jobs microservice within the project architecture.</td>
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
	❯ pip install -r core_requirements.in dev_requirements.in
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
