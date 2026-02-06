from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

#define class for crew
@CrewBase
class ResearchBlog():
    
    # """ResearchBlog crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    #define the path of config files

    agents_config="config/agents.yaml"
    tasks_config="config/tasks.yaml"
    
    # Define agents
    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['report_generator'], # type: ignore[index]
            verbose=True
        )

    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['blog_writer'], # type: ignore[index]
            verbose=True
        )

    # Define tasks
    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_task'], # type: ignore[index]
        )

    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['blog_writing_task'], # type: ignore[index]
            output_file='blogs/blog.md'
        )

    # Define crew
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            tracing=True
        )












    