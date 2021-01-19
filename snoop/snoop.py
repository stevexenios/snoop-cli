import click, time
import compute as COMP

class Recovery(object):
    def __init__(self):
        self.count = 0
        self.compute = False
        self.home_directory = '.'
        


pass_recovery = click.make_pass_decorator(Recovery, ensure=True)


# CONSTANTS for logging to console
COMPUTE_MODE = '\nWe are in compute mode!'
TIME_LOGGING = '\nElapsed time {} seconds'


@click.group()
@click.option('--s', is_flag=True)
@click.option('--compute', is_flag=True)
@click.option('--i', default='../in/reviews.csv', type=click.Path())
@click.option('--o', default = '../out/sitters.csv', type=click.Path())
@pass_recovery
def cli(recovery, s, compute, i, o):
    """
    Main command under which subcommands are grouped into or passed with

    \b
    --s [subcommands]   option to include subcommands.
    --compute           option for executing ranking the sitters.
    --i <input file>    option for denoting input file.
    --o <output file>   option for denoting output file.
    
    \b
    Example command:
    snoop --compute --i reviews.csv --o sitters.csv bark
    """
    recovery.start_time = time.process_time()
    if compute:
        print(COMPUTE_MODE)
        COMP.Compute(i).compute(o) 
    

# Sub-command 1 under cli to print to console
@cli.command()
@click.option('--string', default='World')
@click.option('--repeat', default=3)
# @click.argument('--out', type=click.File('w'), default='../out/sitters.txt', required=False)
@pass_recovery
def bark(recovery, string, repeat):
    """  
    Greetings subcommand to console and text file.

    \b
    --string        <string> person, pet or object to greet.
    --repeat        <n> number oftimes you should be braked at.

    \b
    Example of command:
    snoop --s bark --string Batman --repeat 4
    """
    click.echo('\n' + 'WOOF! ' * 3)
    
    if string:
        click.echo('\nHello %s!' % string)
    if repeat:
        click.echo('\n' + 'WOOF! '*repeat)
    print(TIME_LOGGING.format(time.process_time() - recovery.start_time))
