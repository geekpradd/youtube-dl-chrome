from flask import Flask, request
import subprocess
import os, platform
import config
Windows=False

if platform.system()=="Windows":
    Windows=True

if Windows:
    from savedialog import WindowsSelector as Selector
else:
    from savedialog import LinuxSelector as Selector
app = Flask(__name__)
@app.route('/download' , methods=['POST'])
def start_download():
    url=request.form['url']
    dload(url)
    return 'success'

@app.route('/')
def hello():
    return 'Local server ON'

def dload(url):
   
    #sel=Selector()
    #directory=sel.get_save_dir()
    directory=config.DIRECTORY
    if not Windows:
        sel.kill()
    if directory:
        os.chdir(directory)
    if not Windows:
        subprocess.Popen(['gnome-terminal', '-x', 'youtube-dl',url])
    else:
        if config.WindowsConEmu:
            subprocess.Popen(['ConEmu64', '/cmd ', 'youtube-dl',url])
        else:
            subprocess.Popen(['start', 'youtube-dl',url])
if __name__ == '__main__':
    app.run(debug=True)