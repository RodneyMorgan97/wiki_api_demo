# Github-and-API-Basics
### Tutorial on basic git and API

## Intro/Goals
Welcome to HAkron! Make sure to ***bring a laptop*** so you can follow along with the lesson!

Everything in this guide will be covered in the lesson -- this is just to give you an idea about what we'll cover, or to help you catch up if you miss something that was said. 

The goal of this lesson is to learn how to use Github, set up a repository, and learn some things about API!

## Github - What Is It, and Why Use It?

*If you already know what github is, skip this section.*

Github is for project management!  Here's some reasons to use Github:

  * It allows you to share projects, either with a team or with the whole world, and set permissions on who can and can't contribute.
  * If you don't have permission to edit a project, you can 'fork' it -- make a copy of it -- and edit it all you want
  * Github uses Git, a version control system (like SVN, if you've used that) that lets you work on your projects from any computer, and lets you go between different saved versions anytime you want. 
  * When you have multiple people working on a project, Git also helps handle "merge conflicts" -- when two different users submit two different, conflicting submissions
  * A bunch of other neat organization tools, like issues, wikis, and readme files like this one!!
  
### -- Github Glossary
#### --- Some Github terms you might be confused by:

  * **Git** -- Version control system. You install this on your computer to let you easily move things to and from Github.
  * **Github** -- The website hosting everything submitted by Git. 
  * **Repository (or repo)** -- Any github project. Basically just a set of files hosted on github.
  * **Clone** -- You can take a Github repo and *clone* it to your local computer so you can work on it.
  * **Commit** -- Once you have a local clone of a repo, you can submit a *commit* of your changes back to the parent repo. Each commit is basically a 'version', when we talk about version control.
    * (Note that `git commit` won't submit your code to Github on its own. The full process for committing code is `git add [whatever files were changed]`, `git commit -m "your commit message"`, `git push`. We'll go over this later.)
  

## Github Setup

The first thing we need is to set up a github account. *If you already have a github account, skip this portion.*

Go to [github.com](https://www.github.com) and sign up with a unique username, and an email you can access.

Select the free account option and press continue. Fill out the survey if you'd like, it's optional. You'll now need to confirm your email. 

## Repo Setup

Once you have a confirmed Github account, click on the + icon in the upper lefthand corner of Github, and select "New Repository". 

Name your repository whatever you want -- "My first site" or something.  Add a description, decide whether you want it to be public or not, and check the box that says "initialize this repository with a README".

Congrats, you just made your first Github repo! 

## Git setup/Cloning our repo!

Now, we need to set up Git on your computer. To do this, we're going to learn some basic terminal commands!

### Mac/linux Git Install instructions:

If you're using a Mac or Linux OS, open up the terminal. On a mac, you should be able to find it by searching for "terminal", or looking in your Applications folder.  To see if you have git, type `git --version` and press enter. If you don't have it yet, follow [these instructions](https://www.atlassian.com/git/tutorials/install-git), and then restart your terminal to see if it worked.

### Windows Git Install Instructions:

If you're using a Windows computer, open up Windows Powershell. You should be able to find it by searching for it. (Command Prompt should also work, but I like powershell more.)  To see if you have git, type `git --version` and press enter. If you don't have it yet, follow [these instructions](https://www.atlassian.com/git/tutorials/install-git#windows), and then restart your powershell to see if it worked.

For either setup, remember to do these commands too:
```
 git config --global user.name "Your name"
 git config --global user.email "your@email.com"
 ```

### Cloning the Repo

Now that you have Git installed, we can finally clone our repo! But first, we need to learn how to use our terminal.  

Your terminal always points to somewhere on your computer, and we can type different commands to navigate through our computer and interact with files. (Tip: Pressing 'tab' in the terminal will try to autocomplete whatever you're typing.)

Here are the terminal commands we'll be using:

  * `cd [somewhere]` -- stands for "change directory". Replace `[somewhere]` with an existing folder.
    * `cd ..` will take you back one folder (ex: if you're in `~/Files/myfolder/`, `cd ..` takes you to `~/Files/`)
    * `cd ~` will take you to your "home directory" from wherever you are.
  * `ls` -- is an abbreviation for "list", which doesn't make sense but whatever. It lists all the files and folders in your current directory
  * `mkdir [folder name]` -- stands for "make directory". Will make a folder named `[folder name]` in the current directory

If you type `cd ~/Desktop`, you'll navigate straight to your desktop. From there, navigate to wherever you want to keep your project on your folder. You can also type `mkdir hacksuProjects` or something to make a folder named "hacksuProjects" on your desktop (You would then type `cd hacksuProjects/` to go inside of that folder.)

Once you're in the folder you want to store your projects, go back to your github repo, and click the green 

Go to your repo page on Github and find the green button that says 'Clone or download', and copy the URL it shows. Go back to the terminal and the following command, replacing `[ur]` with the URL you copied:

`git clone [url]`

Unless you have an error, congrats! You just cloned your repo to your computer! You can now enter `cd [repo name]` to go int

# HAkron API demo
# Intro:
Demo of the Wikipedia API with a simple python application
Application takes input from user and returns a summary from wikipedia of the topic

# Install Stuff:
### To install Python 2.7 on Windows: 
Install [here](https://www.howtogeek.com/197947/how-to-install-python-on-windows/) :)

### To install Python 2.7 on macOS: 
First install [Homebrew](https://brew.sh/) :0

Then install Python 2.7 by typing the following in your terminal: 

    brew install python

### Install a text editor:

   * Any of these will work:

    * [Visual Studio](https://code.visualstudio.com/)
    * [Atom](https://atom.io/)
    * [Sublime Text](https://www.sublimetext.com/)
