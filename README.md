# devops-exercise
This project realizes an exercise demonstrating the containerization and deployment of a service.

# Welcome to my DevOps Exercise


## Overview

This exercise demonstrates the integration of **Github**, **Travis-CI**, **Docker** and **AWS ElasticBeanstalk** to build, test and deploy a Python script.

## Prerequisites & Setup
If you were to fork this project, there are several manual steps you would have to complete in order to build out the complete CI/CI pipeline

 - Make sure you have created a [Travis-CI](https://travis-ci.com/) account.  Log in with your Github credentials, and link your Github repo
 - Make sure you have created a [DockerHub](https://hub.docker.com/) account.  Create a repo for your project
 - Make sure you have created an [Amazon Web Services (AWS)](https://aws.amazon.com/) account.  Create an ElasticBeanstalk (EB) application and environment.  You will also want to create an IAM user with adequate EB permissions, and generate and access-key / secret.

You are encouraged to make the following configurations in your environment in order to customize for your project:

 - Define the following environment variables within the **Settings** section of your Travis-CI repo.  They are used to store you credentials to Docker and AWS EB.
![Travis-CI Environment Variables](https://github.com/dnissimi/devops-exercise/blob/master/images/Screen%20Shot%202018-10-15%20at%203.45.43.png?raw=true)
 - Define the appropriate values for the environment variables listed the **.travis.yml** file in the root of this repo
 - Update your **Dockerfile** accordingly.  Note that .travis.yml obtains the Docker version tag form the Dockerfile environment variable **SERVICE_VERSION**.  We encourage using this variable in your Dockerfile.
 - Unit test and other settings (such as python requirements, etc..) may be configured as needed
 
## Usage

Travis-CI is configured by default to begin the build process upon **push** operation to Github repo.

We recommend changing the value of SERVICE_VERSION in the Dockerfile for your branch. 

The files listed within the [.travisignore](https://github.com/dnissimi/devops-exercise/blob/master/.travisignore) file will not trigger a build.

Only a push to the **master branch** will trigger a production deployment to AWS EB.  Other branches will only be built and pushed to DockerHub.

Upon deployment, AWS EB, the service can be accessed at [this URL](http://devopsexercise-env.94vr5xphmw.eu-west-1.elasticbeanstalk.com/api/v1.0/about). 

**NOTE:**  It may take several minutes for your changes to take affect, while AWS launches the new container.


# Sequence diagram

The following  diagram summarizes the flow implemented in this exercise.

```mermaid
sequenceDiagram
Actor ->> Actor: git commit
Actor ->> GitHub: git push -u origin master
GitHub -->> Travis: Push trigger
Travis ->> Travis: Setup / Clone repo
Travis ->> Travis: Build
Travis ->> Travis: Docker Run
Travis ->> Travis: Unit Test
Travis ->> DockerHub: Tag / push Docker image
Travis ->> AWS EB: Deploy Docker container to AWS
