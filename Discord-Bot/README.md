# Project 2

## Setup

1. To start getting an API, head to the discord developer portal and select the OAuth2 tab
    - This process will give your bot access to Discord APIs.
    - Make sure you have the proper dependencies running on your system
    - run `python` or `python3` to see which version of python is running, this bot needs python3
    - run `pip install -U discord.py`
    - run `pip install -U python-dotenv`
    - note you may need to use `pip3` in these commands for them to work  


2. Scroll down the page and check the `bot` box in `SCOPES`, then choose what kind of permissions to give it.
    - A URL will be created at the bottom of the `SCOPES` box, paste it into your browser and select the server you want the bot to be added to.

3. Click `Authorize` and the bot will appear in your server.

4. Inside the same directory as your bot code create a file named `.env`.
    - Inside the `.env` create a variable like this `DISCORD_TOKEN={your-bot-token}`, the {your-bot-token} will be replaced with your bot's OAuth token. Be sure to also get rid of the brackets.

5. Head back to the Developer Portal, click on the `Bot` tab on the left and click copy under `TOKEN` for the bot you want tie to your code.
    - Now go into your `.env` file in the same directory as your bot code and replace `{your-bot-token}` with the copied OAuth token.

6. To protect your token add the `.env` to a `.gitignore` file
    - In your home directory or another directory, create a file named `.gitignore` and put the relative path to your bot directory's `.env` file
    - If your key is exposed, go back to the developer portal and hit regenerate under `TOKEN`, then use `git rm --cached filename` to deal with untracking your `.env`, check your `git status` output, and `push` your changes to Github, then follow step 5 again.  

## Usage

 To start Using the bot you can type one of three commands, `fortune!` will have the bot respond with a random Chinese fortune cookie fortune, `star wars!` will have the bot respond with a random star wars quote, and `sand!` will have the bot reply with Anakin's feelings about sand.

 ## Research

 This bot only currently works when you turn it on and leave that terminal running, depending on what you're using a bot for you might need it to be running all the time. If you need a bot to be constantly running you could turn it in to a screen process. In a screen the bot process can be detached from the session have the screen manage it, the screen session can be attached at a later time and the terminal will be as it was left. Although you still need to start the bot up yourself, unlike making the bot a start up process, it will keep running in screen until you reattach the session and turn it off, so taking the bot offline to make any changes would be easy.
