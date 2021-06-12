# Bash Bot

Interactive bot which can explain basic bash commands.
Comes with a quiz mode.

## Architecture
- CLI frontend
- Raasa backend (+ raasa/rustling)

Raasa backend provides a rest api to the CLI frontend

## Conversation

Start the bot with ```bb <first command>```

### Explain a command (long version)
- User: How can I create a directory?
- Bot: You can use the mkdir command. Should I provide you with an example?
- User: Yes
- Bot: Please give me the name of the directory to create.
- User: foo
- Bot: Use "mkdir foo" to create a directory with the name foo.
- Bot: Bye

### Explain a command (short version)
- User: How can I read a file?
- Bot: You can use the cat command. Should I provide you with an example?
- User: No, I do not need an example
- Bot: Ok, Bye

### Do a quiz

- User: let's do a quiz
- Bot: How to jump into a directory with the name "foo"?
- User: With cd foo.
- Bot: Correct
- Bot: How to read a file with the name "bla".
- User: read bla
- Bot: Wrong! Use "cat bla" to read a file wih the name "bla"
- Bot: That's all. I hope you learned something. 
- Bot: Bye

"Bye" message signals to shut down the cli application.

## Supported commands
- cd
- mkdir
- rm <filename> and rm -rf <directory>
- cat

## Install on machine
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

## Rasa server mode
```rasa run --credentials ./credentials.yml --enable-api --model ./models --endpoint ./endpoints.yml --cors "*" ```

## Install in docker

Build action server container:
```cd bashbot```
```docker build -t action_server -f Dockerfile.action . ```

Build webclient container:
```cd webclient```
```docker build -t webclient . ```

