# Bash Bot

Interactive bot which can explain basic bash commands.
Comes with a quiz mode.


## Supported commands
- cd
- mkdir
- rm <filename> und rm -rf <directory>
- cat

## Install
Spin up a rasa/duckling intance:
```docker run -p 8000:8000 rasa/duckling```

activate virtual env:
```source ./venv/bin/activate```

venv can be deactivated with: ```deactivate``` command

run custom actions:
```rasa run actions```


## Open a rasa shell to test the bot

open rasa shell:
```rasa shell```
