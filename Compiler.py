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
    debug_list = [False, False, False, False, False]

    # scan:parse:semantic:irt:codegen
    for i in range(0, len(debug_split)):
        if debug_split[i] == 'scan':
            debug_list[0] = True
        elif debug_split[i] == 'parse':
            debug_list[1] = True
        elif debug_split[i] == 'semantic':
            debug_list[2] = True
        elif debug_split[i] == 'irt':
            debug_list[3] = True
        elif debug_split[i] == 'codegen':
            debug_list[4] = True

    if target == 'scan':
        token_stream = Lexer.scan(file_name, debug_list)

    elif target == 'parse':
        token_stream, ast = Parser.parse(file_name, debug_list)

    elif target == 'semantic':
        token_stream, ast = Semantic.semantic(file_name, debug_list)

    elif target == 'irt':
        pass

    elif target == 'codegen':
        pass

    else:
        print("Wrong option. Please use --help.")

    f = open(('outputs/' + str(out_name) + '.txt'), "a+")
    for tokenized in token_stream:
        line = str('\n\nlexeme: ' + str(tokenized.lexeme)
                   + '\ntoken: ' + str(tokenized.token)
                   + '\ntype: ' + str(tokenized.token_type)
                   + '\nline_num: ' + str(tokenized.line_num))
        f.write(line)
    f.close()


if __name__ == '__main__':
    cli()

    # lexer dev
    # debug_list = [False, False, True, True, True]
    # token_stream = Lexer.scan('examples/example4.dcf', debug_list)

    # parser dev
    # debug_list = [False, False, True, True, True]
    # ast = Parser.parse('examples/example4.dcf', debug_list)

    # semantic dev
    # debug_list = [False, False, True, True, True]
    # ast = Semantic.semantic('examples/example5.dcf', debug_list)
