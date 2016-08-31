# MultiPlayer
enables multiple players to play serious games like trivia using IOT devices : Amazon ECHO,..

This "Application" contains :
- the usual files for Alexa Skill defining the Interaction Model : custom slots, utterance file, json intent
- the zip archive file containing the lambda files,...
- the python code to be run on Raspberry Pi, in order to display leaderboard. Data is supposed to be returned by some API Gateway (triggering a lambda file), the url of the gateway can be specified as second argument of python program, first one is the python file.

