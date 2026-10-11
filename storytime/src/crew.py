from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import tools

@CrewBase
class StorytimeCrew():
    """storytime crew"""

    # Agent definitions

    @agent
    def newresearcher(self) -> Agent:
        return Agent(
            config=self.agents_config['newresearcher'],
            tools=[tools.query_perplexity, tools.web_scrape],
            verbose=True,
        )

    @agent
    def eminem(self) -> Agent:
        return Agent(
            config=self.agents_config['eminem'],
            verbose=True,
        )

    # Task definitions

    @task
    def get_news(self) -> Task:
        return Task(
            config=self.tasks_config['get_news'],
        )

    @task
    def rap(self) -> Task:
        return Task(
            config=self.tasks_config['rap'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Test crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )