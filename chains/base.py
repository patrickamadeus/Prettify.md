import sys
sys.path.append("..")
from dotenv import load_dotenv
load_dotenv()

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

    # input_path: str = None
    # output_path: str = None

    def __init__(self):
        debug("Initializing PrettifyChain...")
        # self.input_path = input_path
        # self.output_path = output_path
        self.prompt_factory = PromptFactory()
        debug("PrettifyChain initialized.")

    def _construct_chain(self):
        prompts = self.prompt_factory.get_prompts()
        for prompt in prompts:
            self.chains.append(
                LLMChain(
                    prompt=prompt,
                    llm=ChatOpenAI(temperature=0.0),
                )
            )
    
    def _construct_sequence(self, verbose: bool = False):
        self._construct_chain()
        self.sequence = SimpleSequentialChain(
            chains = self.chains, 
            verbose = verbose
        )

    def print_prompts(self, complete: bool = False) -> str:
        d = {}
        for k,v in self.prompt_factory.get_prompt_dict().items():
            if complete:
                d[k] = v.template
            else:
                d[k] = v.template[:200] + "...."
        pprint_dict(d)

    def run(self, input_path: str, output_path: str, verbose_run: bool = False, verbose_cost: bool = False) -> str:
        # Open input file
        markdown_text = open_markdown(input_path)

        if verbose_cost:
            with get_openai_callback() as cb:
                self._construct_sequence(verbose=verbose_run)
                result = self.sequence.run(markdown_text)
                print(cb)
        else:
            self._construct_sequence(verbose=verbose_run)
            result = self.sequence.run(markdown_text)
        
        # Save output file
        text_to_markdown(result, output_path)

        return result