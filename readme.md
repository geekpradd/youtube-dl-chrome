##YouTube DL Chrome Extension

This is a Chrome Extension and Flask Server to open up YouTube DL (which BTW is a terminal YouTube Video downloading utlity). Usage is very simple, just click on the Browser action in Chrome (load the youtube-dl-chrome folder as an extension first and run the Flask Script) and the Terminal should pop open running YouTube DL.

This is the core development repository. All development will done in this fork rather than the main repo.
##Installation

Firstly, download YouTube-DL from <a href="http://rg3.github.io/youtube-dl/download.html"> here</a>.

Download all the files first. You need Flask installed on your Python distribution. Both Python 2.x and 3.x are supported. To install Flask do `pip install flask` and then cd to the directory. Run the server by doing `python localserver.py run`. This will start the server. 

Now, load the extension by going to `chrome://extensions`, tick "Developer Mode" and click Load Unpacked Extension. Select the "youtube-dl-chrome-client" folder and the extension should be loaded.

To test, click on any YouTube Video link and click the extension. A Terminal/Command Prompt/ConEmu should open with youtube-dl running in it.
## What's New?

We've updated the project quite a lot and here are some main changes:

1. Playlist support added
2. Single Config.py file for configurations
3. Support for ConEmu console emulator (which is a million times better than CMD) in Windows

##Configuration

Presently 2 configuration options are available (a quality option will be available soon). You can change them by editing the `www/config.py` file.

1. Directory- Location of the directory where you want to save the videos.

2. WindowsConEmu- Set it to `True` if you want to use ConEmu in place of the Command Prompt on Windows like me.

##To-Do:

1. Add Quality Options to Extension
2. Modify DOM of the YouTube page to display a Download button (with options)


##About

Created By Pradipta (geekpradd)  using HTML5, Javascript, Chrome APIs, Python, Flask and YouTube-DL. Thanks to the kindlyone for the Flask Server.
