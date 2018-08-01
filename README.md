This project is an attempt to streamline / automate the job search process. I am automating applying to job on [Angel](https://angel.co/). I'm going to use Selenium for this, it will open a page in the background and navigate through it. This is going to be a 2 part README, partially so you can get it working, and partially so you can see how the code works - which I guess is the point of all READMEs.

First let's install [Selenium](https://www.seleniumhq.org/):
1. `pip install selenium`
2. Navigate to [this page](http://selenium-python.readthedocs.io/installation.html#drivers) and select the browser you want to use. I chose Chrome, so Google can get more of my data. You'll then download the correct folder (unzip it if needed) and move it to your path. Mine was in my `../Downloads/` folder, and I moved it to `usr/local/bin`: just copy/paste this: `sudo mv chromedriver /usr/local/bin/`

Ok. That's actually kinda everything you need to do to install Selenium.

Next you'll need an [Angel List](https://angel.co/) account. Save your login credentials
to a .csv as `email@email.com,password`. If you end up doing any git related activity with this, add the file to your `.gitignore`. The script will just read those in.

You'll also (currently) need to modify the `html.txt` file to whatever it is when
you select the relevant filter you want in the [jobs page](https://angel.co/jobs). I've uploaded the one I'm using as an example. If you live in Boulder, CO are fine working remotely and want a job as a Data Scientist that is: Full-Time, Contract, or an Internship; you don't need to change this.

Now change the `spiel.txt` file to whatever you want your spiel to be. Keep it around 950 characters, so we can add the recruiter's name to our little cover letter guy. Mine is also included in this repo, as an example. If you feel like trying to get me a job, you can use my cover letter.
