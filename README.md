This project is an attempt to streamline / automate the job search process. I am automating applying to job on [Angel](https://angel.co/). I'm going to use Selenium for this, it will open a page in the background and navigate through it. This is going to be a 2 part README, partially so you can get it working, and partially so you can see how the code works - which I guess is the point of all READMEs.

First let's install [Selenium](https://www.seleniumhq.org/):
1. `pip install selenium`
2. Navigate to [this page](http://selenium-python.readthedocs.io/installation.html#drivers) and select the browser you want to use. I chose Chrome, so Google can get more of my data. You'll then download the correct folder (unzip it if needed) and move it to your path. Mine was in my `../Downloads/` folder, and I moved it to `usr/local/bin`: just copy/paste this: `sudo mv chromedriver /usr/local/bin/`
