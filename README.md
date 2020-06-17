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


