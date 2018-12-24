import click
import os

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

    f=open("{0}/{1}/masterfile.yml".format(path, name), 'w+')
    f.write("# This is the master file.  Don not edit directly")
    f.close()
    
    files = ['parameters', 'storage', 'compute', 'database', 'security', 
    'blockchain', 'analytics', 'management', 'iot', 'media', 'network', 'machine-learning']
    
    for a in files:
        d=open("{0}/{1}/{2}.yml".format(path, name, a), 'w+')
        d.write("# This is the {0} file.".format(a))
        d.close()


if __name__ == '__main__':
    main()