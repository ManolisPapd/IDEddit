# IDEddit
Browse Reddit through a dummy IDE. 

## Table of Contents
* [Usage](#usage)
* [Installation](#installation)
* [Contributing](#contributing)
* [Credits](#credits)
* [Issues to keep in mind](#issues)


## Usage

* Demo


* Written presentation
  1. ```WebSecurityConfig.java``` tab, contains a text area with a Java class that you can modify to hide your browsing to Reddit, switch to this anytime you want.
  2. ```ObjectController.java``` tab, presents a list with 100 posts from /r/popular by default
  3. Type the subreddit name on the search bar next to ```Navigate:``` and press enter
  4. Sort posts by clicking on a radio button, the default sortins is "Hot"
  5. Double click on a post and navigate to ```ObjectService.java``` tab
  6. On ```ObjectService.java``` tab, at the top you can see the title post, below the post body if exists. 
  7. Bottom left, you can see the post url or the link that have been attached by the poster
  8. Bottom right, you can see the current subreddit
  9. At the middle of the scree, you can see the Comments. Click to expand
  10. In each comment, you can also see the upvotes it currently has and at the end of the comment, the username of the commentator.
  11. Comments can be expanded as well to view the replies
  12. Bare in mind, there are limitations to Reddit API and some comments will not be presented.

## Installation
       
* Windows
   * Navigate to the [releases] page and download ```Windows-IDEddit-VERSION.zip``` the latest release.


   * Open the parent folder and run ```IDEddit.exe```.


   * Wait a couple of seconds for the application to start.
       
* Linux
   * Navigate to the [releases] page and download ```Linux-IDEddit-VERSION.zip``` the latest release.


   * Open the parent folder and run ```./IDEddit```.


   * Wait a couple of seconds for the application to start.
       
* All OS
   * Folder ```design``` and configuration ```praw.ini``` should be present with the executable file! You can add your own images, replacing any previous one (with the same name), take care of image dimensions.       
       
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
   
   * pip packages that are needed to be installed: anytree, PyQt5
   * Build:
     * Windows : 
         ``` 
         pyinstaller --clean --win-private-assemblies --noupx --onedir --onefile --hidden-import=anytree --windowed --icon=icon.ico main.py -F --upx-exclude "vcruntime140.dll"
         ```

     * Linux : ```pyinstaller -F main.py --onefile --hidden-import PyQt5.sip``` or ```pyinstaller -F main.py --onefile --hidden-import anytree```. Try both.
   
   
   
  * You are welcome and encouraged to report any issues.
  
  
  
  
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
 
