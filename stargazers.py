from github import Github
import time
import argparse
import json


def main():

    parser = argparse.ArgumentParser("Simple tool to trace your stargazers")
    parser.add_argument("--token", type=str, default=None,
                        help="your Github access token")
    parser.add_argument("--repo", type=str, default=None,
                        help="repo you want to trace")
    parser.add_argument("--target", type=str, default=None,
                        help="target output .csv file")
    parser.add_argument("--sleep", type=int, default=50,
                        help="sleep 1 second after fetching that many stargazers(default: 50)")
    args = parser.parse_args()

    if args.token == None:
        raise ValueError("token should not be None")

    if args.repo == None:
        raise ValueError("repo should not be None")

    if args.target == None:
        raise ValueError("target output file should not be None")

    if ".csv" not in args.target:
        raise ValueError("target file should be a .csv file")

    g = Github(args.token)
    repo = g.get_repo(args.repo)

    all_star = {}
    for index, stargazer in enumerate(repo.get_stargazers()):
        all_star[stargazer.name] = stargazer.location
        if index > 0 and index % args.sleep == 0:
            print(f"sleeping, index = {index}")
            time.sleep(1) 

    with open(args.target, "w") as f:
        json.dump(all_star, f)


if __name__=="__main__":
    main()
