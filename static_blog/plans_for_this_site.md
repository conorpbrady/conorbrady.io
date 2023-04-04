### What I want to do with this site

* Promote myself
* HAve a repository for all my projects
* Blog about what I learn, what I find interesting, blog about building the site
* Writing short stories, things I find interesting in life
* Post a CV that I keep up to date

### Personal site examples

https://xeiaso.net/
https://gwern.net/
https://www.gtf.io/
https://www.brandur.org/about
https://sterlingdemille.com/





### How I build this

* Stack is Django (maybe react FE)
* Write blog posts in markdown - commit, push to GH, have server pick them up and add to db
* Cron job that runs - py script to get all markdown files, tags + metadata in first line
* Run this every 6hrs? Compare against what's in the db, if file is newer update db

* py script imports that in to sqlite database
* No Django admin
* SQLite is fine (nvm no it's not)
* Custom CSS, min JS
* Focus on minimalism / fast loading / reliablity
* Do crazy JS shit in the projects
* Have a gruvbox-esque theme
    * https://github.com/gruvbox-community/gruvbox
