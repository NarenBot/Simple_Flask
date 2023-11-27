### Deploying in ElasticBeanStalk:
- Create a folder and config:  .ebextensions/python.config
- Application file should be "application.py"
- Inside app.run() only host="0.0.0.0"
- Below are the commands for python.config
 ```bash
option_settings:
  "aws:elasticbeanstalk:container:python":
    WSGIPath: application:application
```

Outline: AWS-Codepipeline will get source from Github and deploy it in ElasticBeanStalk.
- Initially create a role of EC2 usecase with ElasticBeanStalk admin-group policy.

ElasticBeanStalk:
- Create an application and environment name in ElasticBeanStalk.
- Choose Python platform with version-3.8
- Add an existing service role (aws-elasticbeanstalk-ec2-role)

CodePipeline:
- Create a pipeline with new service role
- Choose source as Github Version-1 and connect the repository
- Skip the build stage
- Choose deploy as ElasticBeanStalk with environment name.

*****

 ### CI-PUSH_CD-ECR_CD-EC2 (Deployment using Github actions):
 - .github/workflows:main.yaml-> w.r.t AWS [--name=insurance]
 - Create a Dockerfile
 - IAM user: AmazonEC2ContainerRegistryFullAccess | AmazonEC2FullAccess 
 - SecurityCredential -> Create access key with CLI
 - Create repository in ECR
 - EC2 choose instance as Ubuntu with t2.medium
 - Create a key-pair
 - Allow HTTP and HTTPS traffic
 - Need to install the below command in EC2 connect CLI:
    - sudo apt-get update -y
    - sudo apt-get upgrade
    - curl -fsSL https://get.docker.com -o get-docker.sh
    - sudo sh get-docker.sh
    - sudo usermod -aG docker ubuntu
    - newgrp docker
- Goto Github setting -> Actions -> Runner -> Linux
    - Copy all commands and run in EC2 CLI
    - Configure: Enter the runner name : self-hosted
    - Enter 5 Secret variables.
- Finally goto EC2 instance, under security tab -> security-group
    - Edit inbound rules 
    - Add rule as Custom TCP with port 8080 in 0.0.0.0/0