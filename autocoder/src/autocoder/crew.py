import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task


os.environ["OPENAI_API_KEY"] = "NA"


ollama_llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)

@CrewBase
class AutoCoder():
    """Coder crew"""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    @agent
    def coder(self) -> Agent:
        return Agent(
            config=self.agents_config['coder'], 
            verbose=True,
            allow_code_execution=True,
            code_execution_mode='safe',
            max_code_execution_time=30,
            max_Retries=3,
            name='coder', 
            tools=[],
            memory=False,
            llm=ollama_llm  
        ) 
        
    @task
    def code_assignment(self) -> Task:
        return Task(
            config=self.tasks_config['coding_task']
        )  
        
    @crew
    def crew(self) -> Crew:
        return Crew(
            name='AutoCoder', 
            description='A crew of agents that can code and execute code to complete assignments.', 
            agents=[self.coder()], 
            tasks=[self.code_assignment()]
        )