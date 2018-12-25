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
    os.makedirs("{0}/{1}".format(path, name))

    f=open("{0}/{1}/masterfile.yml\n".format(path, name), 'w+')
    f.write("# This is the master file.  Do not edit directly\n")
    f.write('AWSTemplateFormatVersion: "2010-09-09"\n')
    f.close()
    
    files = ['parameters', 'storage', 'compute', 'database', 'security', 
    'blockchain', 'analytics', 'management', 'iot', 'media', 'network', 'machine-learning']
    
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
            d.write("# This is the {0} file.".format(a))
            d.close()
        elif a == 'secuirty':
            d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
            d.write("# This is the {0} file.".format(a))
            d.close()
        elif a =='blockchain':
            d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
            d.write("# This is the {0} file.".format(a))
            d.close()
        elif a == 'analytics':
            d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
            d.write("# This is the {0} file.".format(a))
            d.close()
        elif a == 'management':
            d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
            d.write("# This is the {0} file.".format(a))
            d.close()
        elif a == 'iot':
            d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
            d.write("# This is the {0} file.".format(a))
            d.close()
        elif a == 'media':
            d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
            d.write("# This is the {0} file.".format(a))
            d.close()
        elif a == 'network':
            d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
            d.write("# This is the {0} file.".format(a))
            d.close()
        elif a == 'machine-learning':
            d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
            d.write("# This is the {0} file.".format(a))
            d.close()

if __name__ == '__main__':
    main()