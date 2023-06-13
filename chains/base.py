import sys
sys.path.append("..")

# Langchain & LLM
from langchain.chat_models import ChatOpenAI

# Prompt-related
from langchain.prompts import (
    PromptTemplate,
    load_prompt
)
from templates.factory import PromptFactory

# Chains
from langchain.chains import (
    SequentialChain,
    SimpleSequentialChain,
    LLMChain
)

# Monitoring & Logging
from logging import info, debug, warning
from langchain.callbacks import get_openai_callback

# Utils
from utils.helper import (
    text_to_markdown,
    open_markdown,
    pprint_dict
)
import json

class PrettifyChain():

    chains: [LLMChain] = []
    sequence: SimpleSequentialChain = None
    prompt_factory: PromptFactory = None

    input_path: str = None
    output_path: str = None

    def __init__(self, input_path: str, output_path: str):
        debug("Initializing PrettifyChain...")
        self.input_path = input_path
        self.output_path = output_path
        self.prompt_factory = PromptFactory()
        debug("PrettifyChain initialized.")

    def _construct_chain(self):
        pass

    def print_prompts(self) -> str:
        d = {}
        for k,v in self.prompt_factory.get_prompt_dict().items():
            d[k] = v.template[:200] + "..."
        pprint_dict(d)

    def run(self, markdown_text: str) -> str:
        return