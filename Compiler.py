from stages import Lexer, Parser, Semantic, IRT, Codegen
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('file_name')
@click.option('--target', '-t', default='codegen', help='The target stage for the compiler. It can be: scan, parse, ast, semantic, irt, codegen. The default is codegen.')
@click.option('--debug', '-d', default='', help='List the stages you want to debug separating them with colons, p.e. scan:parse:irt')
@click.option('--opt_stage', '-opt', default='constant', help='In this case, the compilation must reach the phase specified by -target and do only the optimization requested')
@click.option('--out_name', '-o', help='Name for output file, p. e. \'my_file\'.')
def cli(file_name, target, debug, opt_stage, out_name):
    """To run the compiler you must write on the command line:

    EXAMPLES:

        Please refer to the following example to compile a decaf file:

            $ compiler file.dcf --target=scan --out_name=my_output

        or equivalent

            $ compiler file.dcf -t scan -o my_output

        Please note that specifying the target, opt and debug is not necessary as there already exists a default output for these options.

        You could choose to only specify the name of the file and the name of the output file
        """
    click.echo("{}, {}, {}, {}, {}".format(file_name, target, debug, opt_stage, out_name))

    debug_split = debug.split(":")

    debug_stages = []
    print("Debug:")
    for i in debug_split:
        debug_stages.append(i)
        for j in debug_stages:
            j = True
        print('\t'+i+ ':', j)
    print("........................")

    if target == 'scan':
        f = open(('outputs/' + str(out_name) + '.txt'), "a+")
        line = 'Stage: scanning'
        f.write(line)
        f.close()

        print("out name file: ", out_name)
        print("stage target: ", target)
        print("opt_stage: ", opt_stage)
        print("========================")
        print("stage: scanning")

    elif target == 'parse':
        f = open(('outputs/' + str(out_name) + '.txt'), "a+")
        line = 'Stage: parsing'
        f.write(line)
        f.close()

        print("out name file: ", out_name)
        print("stage target: ", target)
        print("opt_stage: ", opt_stage)
        print("stage: scanning")
        print("state: parsing")

    elif target == 'semantic':
        f = open(('outputs/' + str(out_name) + '.txt'), "a+")
        line = 'Stage: semantic'
        f.write(line)
        f.close()

        print("out name file: ", out_name)
        print("stage target: ", target)
        print("opt_stage: ", opt_stage)
        print("========================")
        print("stage: scanning")
        print("state: parsing")
        print("stage: semantic")

    elif target == 'irt':
        f = open(('outputs/' + str(out_name) + '.txt'), "a+")
        line = 'Stage: irt'
        f.write(line)
        f.close()

        print("out name file: ", out_name)
        print("stage target: ", target)
        print("opt_stage: ", opt_stage)
        print("========================")
        print("stage: scanning")
        print("state: parsing")
        print("stage: semantic")
        print("stage: irt")

    elif target == 'codegen':
        f = open(('outputs/' + str(out_name) + '.txt'), "a+")
        line = 'Stage: codegen'
        f.write(line)
        f.close()

        print("out name file: ", out_name)
        print("stage target: ", target)
        print("opt_stage: ", opt_stage)
        print("========================")
        print("stage: scanning")
        print("state: parsing")
        print("stage: semantic")
        print("stage: irt")
        print("stage: codegen")

    else:
        print("Something went wrong!, try again")


if __name__ == '__main__':
    cli()
    # main() o cli()
    # lexer dev
    # debug_list = [False, False, True, True, True]
    # token_stream = Lexer.scan('examples/example4.dcf', debug_list)

    # parser dev
    # debug_list = [False, False, True, True, True]
    # ast = Parser.parse('examples/example4.dcf', debug_list)

    # semantic dev
    #debug_list = [False, False, False, True, True]
    #ast = Semantic.semantic('examples/example4.dcf', debug_list)
