# Auto-Cut EX 
I made an executable file for auto-editor where you open it and select the file rather than typing the file name in the terminal or CMD.

<h2>Step-1:Installing Python3</h2>
For auto-editor to work, you need python 3.13 installed in your system.

<h3>For Windows:</h3>
To download from official source: <a href="https://www.python.org/downloads/release/python-3133/">Click here</a>
<h3>For Linux:</h3>
Run this command in the terminal one by spne, step by step:
<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)"></button>
  <pre><code id="code">
sudo apt install python3
  </code></pre>
</div>

<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)"></button>
  <pre><code id="code">
sudo apt update
  </code></pre>
</div>

<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)"></button>
  <pre><code id="code">
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncurses5-dev libncursesw5-dev xz-utils tk-dev \
libffi-dev liblzma-dev git
  </code></pre>
</div>

<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)"></button>
  <pre><code id="code">
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.13.0/Python-3.13.0.tgz
sudo tar xzf Python-3.13.0.tgz
  </code></pre>
</div>

<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)"></button>
  <pre><code id="code">
cd Python-3.13.0
  </code></pre>
</div>

<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)"></button>
  <pre><code id="code">
sudo ./configure --enable-optimizations
  </code></pre>
</div>

<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)"></button>
  <pre><code id="code">
sudo make -j $(nproc)
  </code></pre>
</div>

<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)"></button>
  <pre><code id="code">
sudo make altinstall
  </code></pre>
</div>

<br><p>To check if the python is installed or not, paste this in terminal:</p>
<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)"></button>
  <pre><code id="code">
python3.13 --version
  </code></pre>
</div>

If your installation was successful, you will this text:
<pre><code>
python3.13.0
</code></pre>

<h2>Step-2:Installing Auto-Editor</h2>
<p>Our video will be cut or edited with auto-editor tool. It is an open source tool that I found in github, <a href="https://github.com/WyattBlue/auto-editor">click here to visit them</a>.</p><br>

<p>##Comment: <i>They use CMD or terminal command to edit your video, I think it is too painful and requires a little bit more time. I don't want to copy my file name and insert it manually there, so I made an executable file to make this process less time consuming and easy.</i></p>

<h3>For Windows:</h3>
Open CMD and run this command:
<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)"></button>
  <pre><code id="code">
pip install auto-editor
  </code></pre>
</div>
This should install the tool, to check if it was installed or not. Run this command:
<div class="code-container">
  <button class="copy-button" onclick="copyCode(this)"></button>
  <pre><code id="code">
auto-editor --help
  </code></pre>
</div>

<h3>For Linux:</h3>
Run these commands, step by step:
<div class="code-container">
  <pre><code>
sudo apt install pipx
  </code></pre>
</div>

<div class="code-container">
  <pre><code>
pipx ensurepath
  </code></pre>
</div>

<div class="code-container">
  <pre><code>
pipx install auto-editor
  </code></pre>
</div>


<h2>Step 3: Making an executable file:</h2>
<h3>For Windows:</h3>
<p>File (.bat) -> <a href="https://files.catbox.moe/1sxgit.bat">Download</a></p>
<br>
<p><b>How it works? (For windows only)</b></p>
<ol>
  <li>Download the above file.</li>
  <li>Make a new folder anywhere you like.</li>
  <li>Move the downloaded file and the video/audio (.mp4/.wav) you want to edit there.</li>
  <li>Double click the downloaded file.</li>
</ol>
<p>After double clicking, CMD will open and do its job. Depending on the video quality and duration, it will sometime.</p><br>
<p><b>Note:</b>This is a .bat file that I made for myself, so the margin is set at 0.2sec; that is the default. 

If you want to modify the margin length, follow the next step!</p>
<p><b>Modify the margin</b></p>
<ol>
  <li>Right click the downloaded file and open with note pad.</li>
  <li>Find "--margin 0.2sec"</li>
  <li>Modify the duration (0.2sec) to you wish. [N.B: I use 0.05sec].</li>
  <li>Save the file (ctrl + s) and close the note pad.</li>
</ol>
<br>
<h3>For Linux:</h3>
<b>Step 1:</b> Put the command in terminal:
<div class="code-container">
  <pre><code>
nano autoeditor-direct.sh
  </code></pre>
</div>
<b>Step 2:</b> Open the .sh file with a text editor, and paste the following:
<div class="code-container">
  <pre><code>
#!/bin/bash

filename=$(zenity --file-selection --filename="$PWD/" --title="Select a video file")

if [ -n "$filename" ]; then
    gnome-terminal -- bash -c "/home/rsk/.local/bin/auto-editor \"$filename\"  --margin 0.05sec; echo; echo 'Done. Press Enter to close...'; read"
else
    zenity --error --text="No file selected."
fi
  </code></pre>
</div>

<b>Step 3:</b> Make it double-clickable from the file manager  
1. Open Nemo (Mint's file manager).  
2. Right-click your <code>autoeditor-direct.sh</code> file → Properties → Permissions → Set "Allow executing file as a program" ✅  
3. Then in Edit → Preferences → Behavior, set "Executable Text Files" to "Ask what to do" or "Run".

<b>Step 4:</b> Install zenity  
<div class="code-container">
  <pre><code>
sudo apt install zenity
  </code></pre>
</div>

<h2>Step 4: Making a desktop app (For LINUX only)</h2>
<b>Step 1:</b> Go to <code>/home/{username}</code> &nbsp;&nbsp;&nbsp;&nbsp; <i># for me it's '/home/rsk'</i>

<b>Step 2:</b> Create a <code>.desktop</code> file (You can set your own custom name) &nbsp;&nbsp;&nbsp;&nbsp; <i># for me it's 'Auto Cut EX.desktop'</i>  
IMPORTANT: Locate your auto-editor with terminal, use:  
<div class="code-container">
  <pre><code>
which auto-editor
  </code></pre>
</div>
(We will use the result in the next step.)

<b>Step 3:</b> Copy and paste this:
<div class="code-container">
  <pre><code>
[Desktop Entry]
Name=Auto Cut EX
Comment=Edit videos automatically
Exec={path to your <code>.sh</code> file}         
Icon={path to your <code>.svg</code> file}
Terminal=true
Type=Application
Categories=AudioVideo;
  </code></pre>
</div>

<b>Example (my version):</b>
<div class="code-container">
  <pre><code>
[Desktop Entry]
Name=Auto Cut EX
Comment=Edit videos automatically for Premiere Pro
Exec=/home/rsk/AutoCut/autoeditor-direct.sh
Icon=/home/rsk/AutoCut/autocut.svg
Terminal=true
Type=Application
Categories=AudioVideo;
  </code></pre>
</div>

<br>
<p>To get my icon -> <a href="https://files.catbox.moe/o5kunf.svg">Download</a></p>
<b>Step 4:</b> Run this in terminal:
<div class="code-container">
  <pre><code>
chmod +x ~/Desktop/Auto\ Cut\ EX.desktop
mv ~/Desktop/Auto\ Cut\ EX.desktop ~/.local/share/applications/
  </code></pre>
</div>
<br>
<p><b>Congrats! You have done it. Now you should see the app in the menu!</b></p>



