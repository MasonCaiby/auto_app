This project is an attempt to streamline / automate the job search process. I am automating applying to job on [Angel](https://angel.co/). I'm going to use Selenium for this, it will open a page in the background and navigate through it. This is going to be a 2 part README, partially so you can get it working, and partially so you can see how the code works - which I guess is the point of all READMEs.

## Setup

First let's install [Selenium](https://www.seleniumhq.org/):
1. `pip install selenium`
2. Navigate to [this page](http://selenium-python.readthedocs.io/installation.html#drivers) and select the browser you want to use. I chose Chrome, so Google can get more of my data. You'll then download the correct folder (unzip it if needed) and move it to your path. Mine was in my `../Downloads/` folder, and I moved it to `usr/local/bin`: just copy/paste this: `sudo mv chromedriver /usr/local/bin/`

Ok. That's actually kinda everything you need to do to install Selenium.

Next you'll need an [Angel List](https://angel.co/) account. Save your login credentials
to a .csv as `email@email.com,password`. If you end up doing any git related activity with this, add the file to your `.gitignore`. The script will just read those in.

You'll also (currently) need to modify the `html.txt` file to whatever it is when
you select the relevant filter you want in the [jobs page](https://angel.co/jobs). I've uploaded the one I'm using as an example. If you live in Boulder, CO are fine working remotely and want a job as a Data Scientist that is: Full-Time, Contract, or an Internship; you don't need to change this.

Now change the `spiel_auto.txt` file and `spiel_manual.txt` to whatever you want your spiels to be. It alternates between the two cover letters, for AB testing. Data Science. Keep it around 950 characters, so we can add the recruiter's name to our little cover letter guy. Mine is also included in this repo, as an example. If you feel like trying to get me a job, you can use my cover letter.

If you want, you can watch a video of it chugging away: [here](https://vimeo.com/282698022).

[<img src="https://raw.githubusercontent.com/MasonCaiby/auto_app/master/pic.png">](https://vimeo.com/282698022)



## What it does

So this script uses Selenium. It first opens a new driver instance (called browser)and navigates to the Angel List login page. It then uses the credentials it pulled from your .csv file and logins into the page. Now it navigates the the URL you saved in your html.txt file. The url should have all relevant filters BE SELECTIVE- Angel list has a limit on the number of open job apps you can have. Then it steps through all `_jm` classes and check to see if it has 'applicants last week' in its text. If so, it clicks on the `<div>` to expand it, clicks on Apply Now, grabs the recruiters name, and puts a message in the `<textarea>` box. Then it clicks Submit or Send or Apply or whatever and moves on to the next one.

Easily the hardest part of all this was figuring out the page structure and how Selenium interacted with it - I've never used Selenium before and I do more Data Science than Web Development. But I learned a lot and I think it works pretty well.

I hope you don't find yourself on the job market anytime soon, but if you do, maybe you can use this to help with your search. I'd recommend putting it in a [schedule](https://github.com/dbader/schedule) function.
