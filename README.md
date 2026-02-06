# ai-report-blog-generator-crewai
A multi-agent content generation workflow using CrewAI to create topic-based research reports and transform them into readable blog content.

🚀 ResearchBlog Crew

Welcome to ResearchBlog Crew, a multi-agent AI project powered by crewAI
.
This repository provides a clean, extensible template for building collaborative AI agents that work together to research, analyze, and generate high-quality written content such as reports and blogs.
The goal of this project is to help you design, configure, and run a production-ready AI crew with minimal setup, while still giving you full flexibility to customize agents, tools, and workflows.

✨ Features

🤖 Multi-Agent Architecture using crewAI
🧠 Clearly defined agent roles, goals, and tools
🧩 Modular configuration via YAML files
📄 Automatically generates research output (report.md)
⚡ Fast and reliable dependency management with UV
🔧 Easy customization and extensibility

📦 Installation
Prerequisites

Python >=3.10 and <3.14
This project uses UV
 for dependency and package management

Step 1: Install UV
If you don’t already have uv installed, run:

pip install uv

Step 2: Install Project Dependencies
Navigate to your project root directory and install dependencies.

(Optional) Lock dependencies and install them using the CrewAI CLI:

crewai install

🔐 Environment Setup

Add your OPENAI_API_KEY into the .env file
This is required for the agents to communicate with OpenAI models.

Example .env file:
OPENAI_API_KEY=your_api_key_here

🛠️ Customization Guide
You can easily tailor the behavior of your AI crew by modifying the following files:

Agents configuration:
src/research_blog/config/agents.yaml


Define each agent’s role, goal, tools, and behavior.

Tasks configuration
src/research_blog/config/tasks.yaml


Specify what tasks the agents should perform and how they collaborate.

Crew logic and tools

src/research_blog/crew.py


Add custom logic, tools, arguments, or workflows for your agents.

Runtime inputs

src/research_blog/main.py


Customize the inputs passed to agents and tasks at execution time.

▶️ Running the Project
To start the AI crew and execute the defined tasks, run the following command from the root directory of the project:

crewai run

What Happens Next?
The research_blog Crew is initialized
Agents are assembled based on agents.yaml
Tasks are executed as defined in tasks.yaml
The final research output is generated as:

report.md


📄 By default, the unmodified example produces a research report on Large Language Models (LLMs) in the root directory.

🧠 Understanding the Crew Architecture

The ResearchBlog Crew is composed of multiple AI agents, each with:
A specific role
A defined goal
Access to relevant tools

These agents collaborate through a structured task pipeline defined in:

config/agents.yaml

config/tasks.yaml

This separation of concerns makes the system:

Easy to reason about

Simple to extend

Ideal for complex, multi-step workflows

📚 Support & Community

If you need help, have questions, or want to contribute:

📖 Read the official documentation:
https://docs.crewai.com

🧑‍💻 Explore or raise issues on GitHub:
https://github.com/joaomdmoura/crewai

💬 Join the Discord community:
https://discord.com/invite/X4JWnZnxPb

🤖 Chat directly with the docs:
https://chatg.pt/DWjSBZn

🌟 Final Note

This project is a powerful starting point for building real-world AI agent systems—whether for research, blogging, automation, or decision-making.

Let’s create wonders together with the power and simplicity of crewAI 🚀
