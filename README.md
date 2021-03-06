# Welcome to my DevOps Exercise


## Overview

This exercise demonstrates the integration of **Github**, **Travis-CI**, **Docker** and **AWS ElasticBeanstalk** to build, test and deploy a Python / Flask application.

## Prerequisites & Setup
If you were to fork this project, there are several manual steps you would have to complete in order to build out the complete CI/CI pipeline

 - Make sure you have created a [Travis-CI](https://travis-ci.com/) account.  Log in with your Github credentials, and link your Github repo
 - Make sure you have created a [DockerHub](https://hub.docker.com/) account.  Create a repo for your project
 - Make sure you have created an [Amazon Web Services (AWS)](https://aws.amazon.com/) account.  Create an ElasticBeanstalk (EB) application and environment.  You will also want to create an IAM user with adequate EB permissions, and generate an access-key / secret.

You should also make the following configurations to your environment in order to customize for your project:

 - Define the following environment variables within the **Settings** section of your Travis-CI repo.  They are used to store your credentials to Docker and AWS EB.

 ![Travis-CI Environment Variables](https://github.com/dnissimi/devops-exercise/blob/master/images/Screen%20Shot%202018-10-15%20at%203.45.43.png?raw=true)
 - Define the appropriate values for the environment variables listed the **.travis.yml** file in the root of this repo
 - Update your **Dockerfile** accordingly.  Note that .travis.yml obtains the Docker version tag form the Dockerfile environment variable **SERVICE_VERSION**.  You must therefor define this variable in your Dockerfile.
 - Unit test and other settings (such as python requirements, etc..) should be configured as needed
 
## Usage

Travis-CI is configured by default to begin the build process upon **push** operation to Github repo.

We recommend changing the value of SERVICE_VERSION in the Dockerfile for your branch. 

Only a push to the **master branch** will trigger a production deployment to AWS EB.  Other branches will only be built and pushed to DockerHub.

For this exercise, the deployed service can be access on AWS EB at [**this URL**](http://devopsexercise-env.94vr5xphmw.eu-west-1.elasticbeanstalk.com/api/v1.0/about). 

**NOTE:**  It may take several minutes for your changes to take affect, while AWS launches the new container.


# Sequence diagram

The following  diagram summarizes the flow implemented in this exercise.

![Sequence Diagram](https://github.com/dnissimi/devops-exercise/blob/master/images/Screen%20Shot%202018-10-15%20at%204.22.51.png?raw=true)
