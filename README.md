# Twilio-Terraform-Project
![alt text](https://github.com/Jurgis325/Twilio-Terraform-Project/blob/main/Twilio_Terraform%20Project(1).png?raw=true)

## About this project
[Twilio](https://www.twilio.com/) is a 3rd party app that allows users to send and process SMS text messages via webhooks.  

This project's goal was to create a terraform file that could deploy an infrastructure on AWS that would allow the user to send a SMS message through Twilio that could start and stop EC2 instances.  It utilizes the following:
- Terraform
- Twilio
- Lambda code written in Python
- a Python script that Terraform runs locally to update the Twilio webhook when deploying
- API Gateway
- VPC
- Security Groups
- Route tables
- Subnets
- EC2 instance
- IAM Roles
- Cloudwatch

## Details
Terraform deploys a VPC called "Main" with two subnets called "Front" and "Back".  An internet gateway and NAT gateway are attached to the "Front" subnet and has route tables associated with it.  A small EC2 instance is deployed to the "Back" subnet with a security group attached that only allows data from port 443.  A lambda function is deployed behind an API gateway that translates information coming to and from Twilio.  Permissions have been given to the Lambda function to control EC2 instances.  Cloudwatch has also been setup to help capture errors. Additionally, there is a script terraform runs that utilizes Twilio's API to update the webhook every time the code is deployed.

When twilio receives a text message, it's forwarded to the API gateway.  The Lambda function checks for a "Start" or "Stop" command and runs a code to start the EC2 instance or stop it respectively.  The Lambda function then returns an acknowledgment of what it's doing.  

This repository does not include the .env file that needs API keys necessary for the upload.
