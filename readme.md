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

install dependecy:
https://pypi.org/project/python-Levenshtein/

## Open a rasa shell to test the bot

open rasa shell:
```rasa shell```

## Rasa server mode
```rasa run --credentials ./credentials.yml --enable-api --model ./models --endpoint ./endpoints.yml --cors "*" ```

## Local docker setup

Build action server and core server container:
```cd bashbot```
```docker build -t action_server -f Dockerfile.action . ```
```docker build -t rasa_bashbot -f Dockerfile.core . ```

Build webclient container:
```cd webclient```
```docker build -t webclient . ```

Run the local docker-compose file:
```docker-compose -f docker-compose.local.yml up ```

Point your browser to localhost:80.

## Setup with containers from dockerhub.
Run the docker-compose file:
```docker-compose -f docker-compose.yml up ```


# TODO
- python-Levenshtein must be installed in action server container. Should be done in dockerfile DONE
- buttons for additional explanation, example or nothing needed DONE
- remove text to speech in webapp DONE
- remove bye response after example DONE
- add support for additional commands (e.g. touch)
- man pages support in container DONE
- man pages documentation should be printed in one response message instead of multiple small messages DONE
- beschreibung beim starten vom bot was er tut (bulletpoints) DONE
- einleitung für quiz. DONE
- quiz verlassbar machen DONE
- erklären bei quiz wie funktioniert DONE
- stop quiz different response DONE
- tts is still active DONE
- handle thank you/thanks message WONT FIX
- dir instead of directory DONE
- docu and doku keywords to needs documetation intent DONE
- exception thrown when documentation is inputed when not in story DONE
- docuemnttation must be written correct. No typos are accepted
- generate random client id DONE
- can duckling be removed ? Removed -> DONE
- catch 500 from rasa -> catch exception, user mesaage that server could not be reached and shutdown DONE/WON't FIX
- filter out EXECUTE command payload before printing DONE
- better detect documentation
- escape special signs e.g. "" in client DONE
- dockerize client and api gw DONE
- test webclient DONE
- create testplan && test everything
- update all containers DONE
- permanet alias for cli client
- api gw does not send example back to webclient before sending no. (malformed json received from api gw) DONE
- create conversation flow diagram DONE
- execute cat does not print file content DONE
- in quiz: exit quiz and exit should abort quiz
- update jar artifact in github 

-------------------------------------------------------------------------

clojure.lang.ExceptionInfo: clj-http: status 400 {:cached nil, :request-time 3, :repeatable? false, :protocol-version {:name "HTTP", :major 1, :minor 1}, :streaming? true, :http-client #object[org.apache.http.impl.client.InternalHttpClient 0x5afcd9c7 "org.apache.http.impl.client.InternalHttpClient@5afcd9c7"], :chunked? false, :type :clj-http.client/unexceptional-status, :reason-phrase "Bad Request", :headers {"Access-Control-Allow-Origin" "*", "Access-Control-Expose-Headers" "filename", "Access-Control-Allow-Credentials" "true", "Content-Length" "188", "Content-Type" "text/html; charset=utf-8", "Connection" "keep-alive", "Keep-Alive" "5"}, :orig-content-encoding nil, :status 400, :length 188, :body "<!DOCTYPE html><meta charset=UTF-8><title>400 — Bad Request</title><style>html { font-family: sans-serif }</style>\n<h1>⚠️ 400 — Bad Request</h1><p>Failed when parsing body as json\n", :trace-redirects []}


-------------------------------------------------------------------------

{"sender": "1a493efb-e2f2-4501-81df-17b30208e4d7", "message": "documentation"}
[]

--------------------------------------------------------------------------

