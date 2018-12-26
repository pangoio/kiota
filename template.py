import os
from os import write
import click

cwd = os.getcwd()

@click.group()
def main():
    pass
@main.command()
@click.argument('name')
@click.option('--path', '-p', default=cwd, required=False, type=click.Path(resolve_path=True), help='Enter the path of where you want to create your project')
@click.pass_context
def template(self, name, path):
    
    pathname = os.path.exists("{0}/{1}".format(path, name))
    if pathname == True:
        print("{0}/{1} already exists".format(path, name))
    else: 
        os.makedirs("{0}/{1}/master".format(path, name))
        f=open("{0}/{1}/master/masterfile.yml".format(path, name), 'w+')
        f.write("# This is the master file.  Do not edit directly\n")
        f.write('AWSTemplateFormatVersion: "2010-09-09"\n')
        f.close()
    
        files = ['parameters', 'storage', 'compute', 'database', 'security', 
        'blockchain', 'analytics', 'iot', 'miscellaneous', 'network', 'machine-learning']
    
        for a in files:
            if a == 'parameters':
                d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
                d.write("# This is the {0} file.\n".format(a))
                d.write("# Store all cloudformation parameters in this file\n")
                d.write("#\n")
                d.write("# Parameters:\n")
                d.close()
            elif a == 'storage':
                d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
                d.write("# This is the {0} file.\n".format(a))
                d.write("# Describe all storage resources in this file.\n")
                d.write("# Storage resources include\n")
                d.write("#\n")
                d.write("# s3\n")
                d.write("# EFS\n")
                d.write("# FSx\n")
                d.write("# s3 Glazier\n")
                d.write("# Storage Gateway\n")
                d.write("#\n")
                d.write("# Resources:\n")
                d.close()
            elif a == 'compute':
                d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
                d.write("# This is the {0} file.\n".format(a))
                d.write("# Describe all compute resources in this file.\n")
                d.write("# Compute resources include\n")
                d.write("#\n")
                d.write("# EC2\n")
                d.write("# Lightsail\n")
                d.write("# ECR\n")
                d.write("# ECS\n")
                d.write("# EKS\n")
                d.write("# Batch\n")
                d.write("#\n")
                d.write("# Resources\n")
                d.close()
            elif a == 'database':
                d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
                d.write("# This is the {0} file.\n".format(a))
                d.write("# Describe all database resources in this file.\n")
                d.write("# Database resources include\n")
                d.write("#\n")
                d.write("# RDS\n")
                d.write("# DynamoDB\n")
                d.write("# Elasticache\n")
                d.write("# Neptune\n")
                d.write("# Amazon Redshift\n")
                d.write("#\n")
                d.write("# Resources:\n")
                d.close()
            elif a == 'secuirty':
                d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
                d.write("# This is the {0} file.\n".format(a))
                d.write("# Describe all secuirty resources in this file.\n")
                d.write("# Security resources include\n")
                d.write("#\n")
                d.write("# IAM\n")
                d.write("# Resource Access Manager\n")
                d.write("# Cognito\n")
                d.write("# Secrets Manager\n")
                d.write("# Certificate Manager\n")
                d.write("# Key Management Service\n")
                d.write("#\n")
                d.write("# Resources:\n")
                d.close()
            elif a =='blockchain':
                d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
                d.write("# This is the {0} file.\n".format(a))
                d.write("# Describe all blockchain resources in this file.\n")
                d.write("# blockchain resources include\n")
                d.write("#\n")
                d.write("# Amazon Managed Blockchain\n")
                d.write("#\n")
                d.write("# Resources:\n")

                d.close()
            elif a == 'analytics':
                d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
                d.write("# This is the {0} file.\n".format(a))
                d.write("Describe all {0} resources in this file\n".format(a))
                d.write("# {0} resources include\n".format(a))
                d.write("#\n")
                d.write("# Athena\n")
                d.write("# EMR\n")
                d.write("# ElasticSearch Service\n")
                d.write("# Kinesis\n")
                d.write("# Data pipeline\n")
                d.write("#\n")
                d.write("# Resources:\n")
                d.close()
            elif a == 'iot':
                d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
                d.write("# This is the {0} file.\n".format(a))
                d.write("Describe all {0} resources in this file\n".format(a))
                d.write("# {0} resources include\n".format(a))
                d.write("#\n")
                d.write("# IoT Core\n")
                d.write("#Amazon FreeRTOS\n")
                d.write("# IoT 1-click\n")
                d.write("# IoT Analytics\n")
                d.write("# IoT Device Defender\n")
                d.write("# IoT Events\n")
                d.write("# IoT Greengrass\n")
                d.write("#\n")
                d.write("# Resources:\n")
                d.close()
            elif a == 'miscellaneous':
                d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
                d.write("# This is the {0} file\n.".format(a))
                d.write("Describe all other resources in this file\n")
                d.write("#\n")
                d.write("# Resources:")
                d.close()
            elif a == 'network':
                d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
                d.write("# This is the {0} file.\n".format(a))
                d.write("Describe all {0} resources in this file\n".format(a))
                d.write("{0} resources include\n".format(a))
                d.write("# {0} resources include\n".format(a))
                d.write("#\n")
                d.write("# VPC\n")
                d.write("# CloudFront\n")
                d.write("# Route 53\n")
                d.write("# API Gateway\n")
                d.write("# Direct Connect\n")
                d.write("#\n")
                d.write("# Resources:\n")          
                d.close()
            elif a == 'machine-learning':
                d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
                d.write("# This is the {0} file.\n".format(a))
                d.write("Describe all {0} resources in this file\n".format(a))
                d.write("{0} resources include\n".format(a))
                d.write("#\n")
                d.write("# Amazon Sagemaker\n")
                d.write("# Amazon Comprehend\n")
                d.write("# AWS DeepLens\n")
                d.write("# Amazon Lex\n")
                d.write("# Machine Learning\n")
                d.write("#\n")
                d.write("# Resources:\n")
                d.close()

        print(""" 
        Kiota skeleton template has been created
        .
        |-- {0}
        |    |-- master
        |    |      |--masterfile.yml
        |    |
        |    |-- parameters.yml
        |    |-- analytics.yml
        |    |-- blockchain.yml
        |    |-- compute.yml
        |    |-- database.yml
        |    |-- iot.yml
        |    |-- machine-learning.yml
        |    |-- miscellaneous.yml
        |    |-- network.yml
        |    |-- storage.yml
        """.format(name))

if __name__ == '__main__':
    main()