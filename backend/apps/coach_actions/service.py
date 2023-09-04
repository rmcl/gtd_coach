from django.conf import settings
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor

from coach_actions.actions import TOOL_ACTIONS

class CoachActionService:
    """Register all available coach actions."""

    SYSTEM_PROMPT = """You are very powerful assistant, with access to the users 'Get Things Done' (GTD) lists. """

    def __init__(self, settings: dict):
        self.settings = settings

        self._openai_api_key = settings.get('OPENAI_API_KEY', None)
        if not self._openai_api_key:
            raise Exception('OPENAI_API_KEY not found in settings')

    def get_agent(self):
        llm = ChatOpenAI(
            temperature=0,
            openai_api_key=self._openai_api_key)

        system_message = SystemMessage(
            content=self.SYSTEM_PROMPT)
        prompt = OpenAIFunctionsAgent.create_prompt(
            system_message=system_message)

        agent = OpenAIFunctionsAgent(llm=llm, tools=TOOL_ACTIONS, prompt=prompt)
        agent_executor = AgentExecutor(agent=agent, tools=TOOL_ACTIONS, verbose=True)
        return agent_executor

    def invoke(self, message : str) -> str:
        agent = self.get_agent()
        result = agent.run(message)
        return result

def get_gtd_coach_service():
    """Get the coach service."""
    return CoachActionService(settings=settings.GTD_COACH)
