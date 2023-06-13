from chains.base import PrettifyChain
import logging

logging.basicConfig(level = logging.DEBUG)

if __name__ == '__main__':
    logging.debug("Prettify.md --- Starting Prettify.md")
    prettify = PrettifyChain(
        input_path="input.md",
        output_path="output.md"
    )
    prettify.print_prompts()

    print("Prettify.md --- Copyright 2023")