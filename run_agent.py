import argparse
from kaggle_environments import evaluate, make

from basic_test_agent import agent

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-train', action='store_true')
    parser.add_argument('-test', action='store_true')
    parser.add_argument('-iters', type=int)
    # parser.set_defaults(feature=True)
    return parser.parse_args()

def main():
    args = parse_input()
    if args.test:
        env = make("halite", debug=True)
        env.run([agent, "random", "random", "random"])
        env.render(mode="html", width=800, height=600)
    elif args.train:
        pass


if __name__ == "__main__":
    main()