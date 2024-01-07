# Get-things-done (GTD) Coach

GTD Coach is a productivity tool inspired by the principles of [Getting Things Done](https://www.amazon.com/Getting-Things-Done-David-Allen-audiobook/dp/B01B6WSK5C) (GTD), by David Allen. This project combines the power of Large Language Models (LLMs) from OpenAI through LangChain, Twilio for SMS integration, and Trello for task management. 

## How it works

The idea behind GTD Coach is to capturing your thoughts and tasks whenever they occur by sending text messages to your coach. In the GTD methodology, this "Capture" phase is crucial- it allows you to focus on one task at a time by capturing the random thoughts or todos somewhere.

You can send text messages to your GTD Coach containing ideas, tasks, or anything you need to remember. The GTD Coach will capture these messages and create trello cards in the list of your choosing.


## Want to host it yourself?

While there are similar services available, I created GTD Coach because I wanted to control my data. By hosting your own instance, you retain full control over your data, eliminating concerns about sharing sensitive information with third-party services.

Prerequisites
To run your own GTD Coach instance, you'll need the following:

* Hosting Environment:

Choose a platform to host a container running Django and a database. Services like Render are recommended, but any host with the necessary capabilities will suffice. Ensure that the host provides a public URL/IP for Twilio webhook integration.

* Twilio Account:

Sign up for a Twilio account to interface with the SMS system effortlessly. Keep in mind that Twilio may charge a nominal fee for each text message sent.

* Trello Account:

GTD Coach integrates with Trello for task management. If you're already using Trello for your GTD system, you're all set. Alternatively, consider other platforms like Notion if you're contemplating a switch.
