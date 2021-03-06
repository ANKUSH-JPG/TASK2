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


NOW LETS HAVE A LOOK AT THE JOB:
The job will use github webhooks to trigger itself , we also created a downstream project of job1 which will be executed once job1 executes successfully.

![Screenshot (451)](https://user-images.githubusercontent.com/51692515/84980026-98f54e00-b14e-11ea-90c4-56c29ad06e27.png)


![Screenshot (452)](https://user-images.githubusercontent.com/51692515/84980030-9bf03e80-b14e-11ea-897c-fe799e894dbf.png)

This will automatically download the files for us that had been pushed to repo by the developer.

 # job 2 :(to look and identify the code)
 
 1. Here we actually identified the extension of the code and created a respective image container for the testing and deployment purpose. This job was the downstream project for job1 i.e it will automatically be triggered once job1 execute successfully.
 
 2. In the execute shell we wrote the acctual code to be implemented. we changed the directory to " /var/lib/jenkins/workspace/job1_github" which was the working directory for job1 . We checked the status code of " ls -a | grep .php " command , if it was 0 that means the file matched and the respective php testing and the deployment server was started. In case the code was 1 , the file was not found.
 
 ![Screenshot (453)](https://user-images.githubusercontent.com/51692515/84980651-42890f00-b150-11ea-8bd1-f4714fa5ddb2.png)
 
![Screenshot (454)](https://user-images.githubusercontent.com/51692515/84980657-44eb6900-b150-11ea-9056-b75f8c62e041.png)


 # job 3:(testing our app on the testing servers)
 
 1. This job was the downstream project for job2 i.e once the file extension is identifed the file will be deployed on testing servers for testing purpose. 
 
 2. We identified the status code of the file on server , if it was 200 the file was working fine on the testing servers and is ready to be deployed on deployment servers. The file was then copied to the folder that was mounted on the deployment server and a "exit 1" command was given to stop the job. The downstream project job5 was activated , that will continoustly monitor the deployment servers and  immediately starts a new server for us if the first one fails. 
 if the status code of the file on server wasnt equal to 200 ,it automatically activates the downstream project job4 (which will send the mail to the developer with the ERROR message).
 
 ![Screenshot (455)](https://user-images.githubusercontent.com/51692515/84981579-79602480-b152-11ea-9545-d387268b88ef.png)
 
![Screenshot (456)](https://user-images.githubusercontent.com/51692515/84981584-7a915180-b152-11ea-9118-b37c38bade1d.png)

# job 4:(mailing to developer)

1. we created code to mail developer , found the status code of the file in testing server and copied it in a file named "error.txt"
. In our mail.py file we opened the error.txt file and mailed it to developer.

![Screenshot (457)](https://user-images.githubusercontent.com/51692515/84982086-8cbfbf80-b153-11ea-867b-77989879d495.png)

![Screenshot (458)](https://user-images.githubusercontent.com/51692515/84982106-977a5480-b153-11ea-8f48-7f98b320b6d6.png)

# job 5:(monitoring the container)

1. For this job we have a upstream project job3 , which we build stable or unstable will trigger this job .

2. The purpose of this job is to continously monitor the deployment container . We created an infinite while loop , inside loop if the current state of the container will be "true" then it is working fine and if the state is "false " that means the container stopped running and a new deployment container will be created behind the scene automatically.

![Screenshot (459)](https://user-images.githubusercontent.com/51692515/84984003-96e3bd00-b157-11ea-96c5-c5985cf7cdca.png)

![Screenshot (460)](https://user-images.githubusercontent.com/51692515/84984008-99461700-b157-11ea-954f-c1a8468e11c0.png)


# NOW LET'S HAVE A LOOK AT THE ACTUAL WORKING:

# IN CASE THE CODE IS RIGHT:

1. job1 will run.
2. job2 will run.
3. job3 will run and fail because the code is working fine.
4. job5 will run and monitor the container.

# ********************************************************************************************************************************



![Screenshot (461)](https://user-images.githubusercontent.com/51692515/84985356-37d37780-b15a-11ea-9e85-e001b14d16ef.png)

![Screenshot (462)](https://user-images.githubusercontent.com/51692515/84985357-3904a480-b15a-11ea-8a51-fcecee46233e.png)

![Screenshot (463)](https://user-images.githubusercontent.com/51692515/84985358-399d3b00-b15a-11ea-9ec8-19e2d5233c36.png)

![Screenshot (464)](https://user-images.githubusercontent.com/51692515/84985360-3a35d180-b15a-11ea-93c3-a0c4bfdbfd92.png)

![Screenshot (465)](https://user-images.githubusercontent.com/51692515/84985363-3b66fe80-b15a-11ea-8a48-3e743231f12b.png)

![Screenshot (467)](https://user-images.githubusercontent.com/51692515/84985342-330ec380-b15a-11ea-8f64-9e2ef10b9184.png)

![Screenshot (466)](https://user-images.githubusercontent.com/51692515/84985365-3bff9500-b15a-11ea-98e0-9ea6e0ed10bf.png)

![Screenshot (470)](https://user-images.githubusercontent.com/51692515/84985353-373ae100-b15a-11ea-8072-9e962866acf0.png)

![Screenshot (468)](https://user-images.githubusercontent.com/51692515/84985345-34d88700-b15a-11ea-95f0-017da114a37c.png)

![Screenshot (469)](https://user-images.githubusercontent.com/51692515/84985349-3609b400-b15a-11ea-9194-2ab5b17ab987.png)


# ********************************************************************************************************************************


# IN CASE THE CODE PUSHED IS WRONG:

1. job1 will run.
2. job2 will run.
3. job3 will run .
4. job4 will run and sent mail.
4. job5 will run and monitor the container.

# ********************************************************************************************************************************

![Screenshot (471)](https://user-images.githubusercontent.com/51692515/84986690-98fc4a80-b15c-11ea-98ed-78e214654cd0.png)

![Screenshot (472)](https://user-images.githubusercontent.com/51692515/84986691-9994e100-b15c-11ea-846e-41db99c7766b.png)

![Screenshot (478)](https://user-images.githubusercontent.com/51692515/84986700-9c8fd180-b15c-11ea-946b-54671afda66c.png)

![Screenshot (477)](https://user-images.githubusercontent.com/51692515/84986697-9b5ea480-b15c-11ea-93cc-4447b481f01d.png)

![Screenshot (473)](https://user-images.githubusercontent.com/51692515/84986694-9ac60e00-b15c-11ea-95b0-b0b2e7660d24.png)

![Screenshot (481)](https://user-images.githubusercontent.com/51692515/84986703-9e599500-b15c-11ea-8caa-a68feeab0704.png)

![Screenshot (480)](https://user-images.githubusercontent.com/51692515/84986701-9d286800-b15c-11ea-9de3-8cd278928167.png)

![Screenshot (482)](https://user-images.githubusercontent.com/51692515/84986705-9ef22b80-b15c-11ea-8324-c8158f5d6323.png)

![Screenshot (483)](https://user-images.githubusercontent.com/51692515/84986674-913ca600-b15c-11ea-8f72-a361d24a4883.png)

![Screenshot (484)](https://user-images.githubusercontent.com/51692515/84986678-926dd300-b15c-11ea-84cb-2f111fb0b1ac.png)

![Screenshot (485)](https://user-images.githubusercontent.com/51692515/84986679-93066980-b15c-11ea-939b-7e45b1f0b6e1.png)


# ********************************************************************************************************************************


