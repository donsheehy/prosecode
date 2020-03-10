import click
import prosecode.tangle
import prosecode.weave

@click.group()
def cli():
    pass

@cli.command()
@click.argument('mdfile')
@click.option('--srcdir', default = './',
                help='Where to put the generated source code.')
def tangle(mdfile, srcdir):
    prosecode.tangle.tangle(mdfile, srcdir)
    click.echo('Tangled the code in ' + mdfile + '.')
    click.echo('Placed the code in ' + srcdir + '.')

@cli.command()
@click.argument('mdfile')
@click.option('--execute', default = False, help='Should the code chunks be executed?')
@click.option('--outfile', default = False, help='The file to save to.')
def weave(mdfile, execute, outfile):
    if outfile == False:
        outfile = mdfile.replace('.md', '.tex')
    prosecode.weave.latexweave(mdfile, execute)
    click.echo('Wove the code.')
