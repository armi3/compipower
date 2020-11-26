from stages import Lexer, Parser, Semantic, IRT, Codegen, Parser_ex
import click


@click.command()
@click.argument('file_name')
@click.option('--target', '-t', default='codegen', help='The target stage for the compiler. It can be: scan, parse, ast, semantic, irt, codegen. The default is codegen.')
@click.option('--debug/--no-debug', default=False, help='List the stages you want to debug separating them with colons, p.e. scan:parse:irt')
@click.option('--out_name', '-o', help='Name for output file, p. e. \'my_file\'.')
def cli(file_name, target, debug, out_name):
    """To run the compiler you must write on the command line:

   compiler <filename.dcf> --target=<target> -o <filename_out>
        """
    click.echo("{}, {}, {}, {}".format(file_name, target, debug, out_name))

    if target == 'scan':
        token_stream = Lexer.scan(file_name, debug)

        f = open(('outputs/' + str(out_name) + '.txt'), "a+")

        for tokenized in token_stream:
            line = str('\n\nlexeme: ' + str(tokenized.lexeme) + '\ntoken: ' + str(tokenized.token) + '\ntype: ' + str(tokenized.token_type) + '\nline_num: ' + str(tokenized.line_num))
            f.write(line)
        f.close()

    elif target == 'parse':
        stack_parser = Parser.scan(file_name, debug) # En caso de tener scan

        f = open(('outputs/' + str(out_name) + '.txt'), "a+")

        for stack in stack_parser:
            line = str('\n\nstate type: ' + str(stack.state_type) + '\ntoken stack: ' + str(stack.token_stack) + '\nstate stack: ' +
                stack.state_stack)
            f.write(line)
        f.close()

    elif target == 'semantic':
        pass

    elif target == 'irt':
        pass

    elif target == 'codegen':
        pass

    else:
        print("Wrong or no target defined")


if __name__ == '__main__':
    #main()
    # lexer dev
    cli()
    #token_stream = Lexer.scan('examples/example2.dcf', True)
