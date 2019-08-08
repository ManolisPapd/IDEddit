# IDEddit
Browse Reddit through a dummy IDE. 

## Table of Contents
* [Usage](#usage)
* [Installation](#installation)
* [Contributing](#contributing)
* [Credits](#credits)
* [Issues to keep in mind](#issues)




## Installation
Currently, this application can run only on Windows autonomously. On Linux, you can download the source code and run `main.py`. See [Contributing](#contributing)

* Windows: 

       * Navigate to [releases] page and download the latest release.
       * Open the parent folder and run ```IDEddit.exe```.
       * Wait a couple of seconds for the application to start.
       
       
       
       
## Contributing
  * In order to contribute or make changes in general, create an app on reddit and then add your account details to the file ```mypackage/__init__.py``` .
  
     **How the file should look like:**
   ```python
     import praw

     handler = praw.Reddit(
       client_id='',
       client_secret='',
       username='',
       password='',
       user_agent=''
     )
   ```
  * You are welcomed and encouraged to report any issues.
  
  
  
  
## Credits
  * [PyQT5] (GUI for the application)
  * [PRAW] (wrapper for Reddit API) 
  * [anytree] (helped a lot while parsing comments from posts) 
  * [Class] (Java class that has been used as an example)
  
  
  
  
  
## Issues
  * The application can crash if there are a lot of requests 
  * Some comments won't be displayed due to Reddit API limitations, more info [here] 
  * On smaller screens, some widgets will appear to override each other. This won't affect the core application.

[//]: #
   [PyQT5]: <https://github.com/baoboa/pyqt5>
   [PRAW]: <https://github.com/praw-dev/praw>
   [anytree]: <https://github.com/c0fec0de/anytree>
   [here]: <https://github.com/praw-dev/praw/issues/1043#issuecomment-471233284>
   [releases]: <https://github.com/mpapd/IDEddit/releases>
   [Class]:                    <https://github.com/openjdk/jdk/blob/master/src/java.desktop/windows/classes/com/sun/java/swing/plaf/windows/AnimationController.java>
 
