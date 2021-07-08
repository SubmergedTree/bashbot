# BashBot


```
 ________  ________  ________  ___  ___  ________  ________  _________   
|\   __  \|\   __  \|\   ____\|\  \|\  \|\   __  \|\   __  \|\___   ___\ 
\ \  \|\ /\ \  \|\  \ \  \___|\ \  \\\  \ \  \|\ /\ \  \|\  \|___ \  \_| 
 \ \   __  \ \   __  \ \_____  \ \   __  \ \   __  \ \  \\\  \   \ \  \  
  \ \  \|\  \ \  \ \  \|____|\  \ \  \ \  \ \  \|\  \ \  \\\  \   \ \  \ 
   \ \_______\ \__\ \__\____\_\  \ \__\ \__\ \_______\ \_______\   \ \__\
    \|_______|\|__|\|__|\_________\|__|\|__|\|_______|\|_______|    \|__|
                       \|_________|                                      
                                                                         
```                                                                         



Interactive bot which can explain basic bash commands.
It can quiz your bash knowledge.
Comes with a web and a cli client.

![CLI Client](images/cliclient.PNG?raw=true "CLI Client")
![Web client](images/webclient.PNG?raw=true "Web client")


## Architecture
- CLI frontend
- Web frontend
- Rasa backend: NLP model
- API Gateway: connects frontends to rasa.

![Components](images/components.PNG?raw=true "Components of Bashbot")

## Dialog flow

![Dialog Flow](images/dialog_flow.png?raw=true "Dialog Flow")


## Supported commands
- cd
- mkdir
- rm <filename> and rm -rf <directory>
- cat

## Install
### Requirements:
- Docker
- For CLI client: Java Runtime Environment

1. Clone this repository
2. run: ```docker compose up```
3. Webclient: Point your browser to localhost:80

For CLI client:
1. Get Jar from https://github.com/SubmergedTree/bashbot/releases/tag/v0.3
2. run: ```docker compose up```
3. Optional: create alias for bashbot cli client for easy access


## Development setup
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

## API Gateway and CLI client
See readmes in api_gw and bashbot_client subfolder.

## Webclient
Static files are served through NGINX.

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

Point your browser to localhost:80