from chains.base import PrettifyChain
import logging

# logging.basicConfig(level = logging.DEBUG)

if __name__ == '__main__':
    logging.debug("Prettify.md --- Starting Prettify.md")
    prettify = PrettifyChain()

    # prettify.print_prompts(complete=True)
    _ = prettify.run(
        input_path = "./data/input/2.md",
        output_path = "./data/output/res_newest.md",
        verbose_cost=True
    )

    print("Prettify.md --- Copyright 2023")