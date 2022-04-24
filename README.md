# COMP247-Group7-Final-Project
COMP247 Group 7 Final Project Deployment

You could upload your website in Heroku using Github. But there is a security issue regarding this method. You can read in detail about it here. So until they solve this issue you have to use Heroku CLI to upload your website. To do this follow these steps: 

heroku login

This will say you to log in to your account. After logging in.  You have to create a remote Heroku repository: 

heroku create -a app-name

To check that a remote named Heroku has been set for your app do this: 

git remote -v

And if you already have a repository on Github, you need to run a new remote by running: 

heroku git:remote -a app-name

Now to deploy your code to Heroku, use the git push command with Heroku: 

git push heroku main

Whenever you want to deploy the latest committed version of your code to Heroku use this command. This command will only affect the code you push to the master or main branches. Heroku remote has no effect on other branches.
