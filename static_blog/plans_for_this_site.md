### What I want to do with this site

* Promote myself
* HAve a repository for all my projects
* Blog about what I learn, what I find interesting, blog about building the site
* Post a CV that I keep up to date


### How I build this

* Stack is Django (maybe react FE)
* Write blog posts in markdown - commit, push to GH, have server pick them up and add to db
* Cron job that runs - py script to get all markdown files, tags + metadata in first line
* py script imports that in to sqlite database
* No Django admin
* SQLite is fine
