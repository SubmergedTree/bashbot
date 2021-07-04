# Testplan:
## CLI Client:

### Einzelne Wörter
- Rauschen Eingeben: dfsdfsdf fooo 3423tg54 " 
- Documentation
- Example
- mkdir cat rm -rf rm
- Hi Hello Good Morning
- How are you ? 
- What are you ? 
- What can you do ? 
- What is your purpose
- What
- How
- Bye
- See you

- Whitespaces, Enter

### Quiz
- Start quiz
- lets quiz
- start a quiz
- quiz
- ask me 
- <"\>
- "ask me"
- \\"foo<
- questions
- In Quiz: exit quiz, stop quiz, stop, exit
- play quiz eqch answer is wrong
- play quiz eqch answer is correct

### Ask commands
- How to create a directory?
- Create a directory ? 
- Directory ? 
- explain create direcotry
- create dir

- How to remove a directory?
- remove a directory ? 
- remove Directory
- explain remove directory
- remve diectory
- remove dir

- How to remove a file?
- remove a file ? 
- remove File
- explain remove file
- remove fle
- remov file
- remove text file

- How to read a file?
- rad a file ? 
- read file
- explain read file
- file
- refd fle
- read text file

- read a directory
- read directory


- For each:
    - Open Documentation: Docs, Docu, Documentation, Documentaition, Documentaion
    - Example, Exapmle, ex
    - I am fine, fine, stop, exit, done

- Execute
    - yes ok yea  -> OK
    - no, i am fine, stop -> OK


## Webclient:

### Einzelne Wörter
- Rauschen Eingeben: dfsdfsdf, fooo, 3423tg54, ", , ,  dfdf \n sdsds \" "\"
    -> Hey! Please ask me about bash commands or for a quiz.
    -> " HTTP 500 (no message shown on webclient -> OK)
    -> \" "\" HTTP 500 (no message shown on webclient -> OK)
- Documentation
    -> I am Bashbot.
I can explain you basic usage of the bash shell.Also I can challenge your bash knowledge. Ask me for a quiz
- dokumentaion
    -> Hey! Please ask me about bash commands or for a quiz.
- Example
    -> Please tell me what you want to do. Then I can give you an example
- mkdir, cat, rm, -rf rm
    -> Hey! Please ask me about bash commands or for a quiz.
- cat, rm, -rf rm
    -> Bye
- Hi Hello Good Morning
    -> Bye
- Hi, Hello, Good, Morning
    -> Hey! Please ask me about bash commands or for a quiz.
- How are you ? 
    -> I am Bashbot.
    I can explain you basic usage of the bash shell.
    Also I can challenge your bash knowledge.
Ask me for a quiz
- What are you ? 
    -> I am Bashbot.
    I can explain you basic usage of the bash shell.
    Also I can challenge your bash knowledge.
    Ask me for a quiz
- What can you do ? 
    ->I am Bashbot.
I can explain you basic usage of the bash shell.
Also I can challenge your bash knowledge.
Ask me for a quiz
- What is your purpose
    -> I am Bashbot.
I can explain you basic usage of the bash shell.
Also I can challenge your bash knowledge.
Ask me for a quiz
- What
    -> I am Bashbot.
I can explain you basic usage of the bash shell.
Also I can challenge your bash knowledge.
Ask me for a quiz
- How
    -> I am Bashbot.
I can explain you basic usage of the bash shell.
Also I can challenge your bash knowledge.
Ask me for a quiz
- Bye
    -> Bye
- See you
    -> Bye

- Whitespaces, Enter
    -> (OK)

### Quiz
- Start quiz 
    -> Ok. Let's do a quiz! I will ask you some questions about basic bash commands.
- lets quiz
    -> Ok. Let's do a quiz! I will ask you some questions about basic bash commands.
- start a quiz
    ->  Ok. Let's do a quiz! I will ask you some questions about basic bash
- quiz
    -> Ok. Let's do a quiz! I will ask you some questions about basic bash
- ask me 
    -> Ok. Let's do a quiz! I will ask you some questions about basic bash
- "ask me"
    -> HTTP 500
- questions
    -> Hey! Please ask me about bash commands or for a quiz.
- In Quiz: exit quiz (not aborted), stop quiz (aborted), stop (aborted), exit (not aborted)
- play quiz eqch answer is wrong
    -> OK
- play quiz eqch answer is correct
    -> OK

### Ask commands
- How to create a directory? -> OK
- Create a directory ?  -> OK
- Directory ? -> Bye (could be better)
- explain create direcotry
- create dir -> Hey! Please ask me about bash commands or for a quiz. OR interpreted as example

- How to remove a directory? -> I am Bashbot.
I can explain you basic usage of the bash shell.
Also I can challenge your bash knowledge.
Ask me for a quiz
- remove a directory ?  -> OK
- remove Directory -> Bye
- explain remove directory
- remve diectory -> Hey! Please ask me about bash commands or for a quiz.
- remove dir -> Hey! Please ask me about bash commands or for a quiz.
- delelete a folder -> NO
- delete a directory -> NO

- How to remove a file? -> I am Bashbot.
I can explain you basic usage of the bash shell.
Also I can challenge your bash knowledge.
Ask me for a quiz
- remove a file ? -> OK
- remove File -> OK
- explain remove file -> OK
- remove fle -> Hey! Please ask me about bash commands or for a quiz.
- remov file -> Hey! Please ask me about bash commands or for a quiz.
- remove text file -> OK
- delete a file -> does not work

- How to read a file? -> OK
- rad a file ? -> OK
- read file -> OK
- explain read file  -> OK
- file -> No answer
- refd fle -> Hey! Please ask me about bash commands or for a quiz. (is ok)
- read text file -> OK

- read a directory -> bye 
- read directory -> bye

- How to create a directory? and read a file -> I am a bot, powered by Rasa.

- For each:
    - Open Documentation: Docs (No), Docu, Documentation, Documentaition, Documentaion -> Broken
    - Example -> OK
    - I am fine (OK), fine (OK), stop (No), exit (No), done (No)