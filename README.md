# Musload
Python based app to download youtube content in audio or video format

 * [Installation](#Installation)
 * [Usage](#Usage)


<a id="Installation"></a>

#Installation

To use Musload there are a few dependencies that must be taken care:

1) youtube-dl:

To install it right away for all UNIX users (Linux, OS X, etc.), type:

sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl

If you do not have curl, you can alternatively use a recent wget:

sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl

Windows users can download an .exe file and place it in any location on their PATH except for %SYSTEMROOT%\System32 (e.g. do not put in C:\Windows\System32).

You can also use pip:

sudo -H pip install --upgrade youtube-dl

This command will update youtube-dl if you have already installed it. See the pypi page for more information.

OS X users can install youtube-dl with Homebrew:

brew install youtube-dl

Or with MacPorts:

sudo port install youtube-dl

Alternatively, refer to the developer instructions for how to check out and work with the git repository. For further options, including PGP signatures, see the youtube-dl Download Page.


2) urllib2: Install this python based library using pip

<a id="Usage"></a>

#Usage

To use Musload follow the below mentioned steps:

1) Create a list with names of the content in the input.txt file

2) Enter into sudo mode using 
```sh
'sudo -s'
```

3) Run the script using 
```sh
'python musload.py'
```

4) All the required content should be downloaded in the Output folder 
