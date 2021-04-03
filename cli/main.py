from cli.json_parser import JsonParser
import sys
import json

from cli.runner import Runner


def run():
    if len(sys.argv) < 2:
        print("Program must be called with an input json.\nRead the README for more information")
        return
    else:
        json = JsonParser.load_file(sys.argv[1])
        runner = Runner.build(json)

    runner.run()


if __name__ == "__main__":
    run()
