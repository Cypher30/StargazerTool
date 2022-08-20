# StargazerTool
This is a light weight tool to track the Github repo's stargazers' location

usage:
```bash
Simple tool to trace your stargazers [-h] [--token TOKEN] [--repo REPO] [--target TARGET] [--sleep SLEEP]

optional arguments:
  -h, --help       show this help message and exit
  --token TOKEN    your Github access token
  --repo REPO      repo you want to trace
  --target TARGET  target output .csv file
  --sleep SLEEP    sleep 1 second after fetching that many stargazers(default: 50)
  ```

Currently this tool will dump a dictionary to the target csv file, each key-value pair denotes the username-location pair.

TODO:
1. Draw those things on a map