#  TASK2
# DEPLOYING THE PHP CODE ON PRODUCTION SERVER AND MONITORING THE CONTAINER.

# TASK COMPLETED IN SHORT:
 1. Create container image that’s has Jenkins installed  using dockerfile 

 2. When we launch this image, it should automatically starts Jenkins service in the container.

 3. Create a job chain of job1, job2, job3 and  job4 using build pipeline plugin in Jenkins 

 4.  Job1 : Pull  the Github repo automatically when some developers push repo to Github.

 5.  Job2 : By looking at the code or program file, Jenkins should automatically start the respective language interpreter install image   container to deploy code ( eg. If code is of  PHP, then Jenkins should start the container that has PHP already installed ).

 6. Job3 : Test your app if it  is working or not.

 7. Job4 : if app is not working , then send email to developer with error messages.
 
 # TASK IN DETAIL:
 # creating the dockerfile to install the jenkins:
   1. The first need was to create the dockerfile which has the required softwares to be installed in a container image so that we can run a container from it. so i created a dockerfile which has jenkins and docker installed and on running container from that image, the jenkins and docker server also starts.
   
 ![Screenshot (443)](https://user-images.githubusercontent.com/51692515/84906563-bfc06f80-b0cf-11ea-8b9a-c5450dea860a.png)
 
 2. I created a image named jenkins:o with this docker file.
 
 ![Screenshot (444)](https://user-images.githubusercontent.com/51692515/84906818-0dd57300-b0d0-11ea-961f-6c76ef0857a0.png)


# next is to launch the image :
 1. when we launched the image , jenkins service automatically started in the container and the token was given to us in order to login to jenkins.
 
![Screenshot (445)](https://user-images.githubusercontent.com/51692515/84907856-57728d80-b0d1-11ea-9eb1-7196084b0c78.png)
 
 
![Screenshot (446)](https://user-images.githubusercontent.com/51692515/84907866-5b061480-b0d1-11ea-8df7-1b654e650112.png)

2. On running the jenkins we got :

![Screenshot (447)](https://user-images.githubusercontent.com/51692515/84908054-9a346580-b0d1-11ea-8e02-7afc0574fa9b.png)

# create the job chain in jenkins using the build pipeline:

THE BUILD PIPELINE CREATED LOOKS LIKE :

![Screenshot (450)](https://user-images.githubusercontent.com/51692515/84910240-4414f180-b0d4-11ea-8181-1a6ca6e58b37.png)


# NOW LET US EXPLAIN EACH AND EVERY JOB ONE BY ONE
  # job 1 :( to pull the code from git hub)
  
  1. We created a php file which had the code to be deployed and a mail.py file which will be used later in case the code fails to execute on the testing servers.
  
  ![Screenshot (448)](https://user-images.githubusercontent.com/51692515/84908756-7e7d8f00-b0d2-11ea-96f7-283aed12fec7.png)
  
we also created a post-commit file that would automatically push the code to the repo present in github. On github we changed the webhook settings and created a hook there that would automatically trigger the jenkins job .

![Screenshot (449)](https://user-images.githubusercontent.com/51692515/84909991-f7311b00-b0d3-11ea-9ae2-588c2b40f36d.png)


