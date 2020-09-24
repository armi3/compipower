import Scanner
import click


@click.command()
@click.argument('file_name')
@click.option('--target', '-t', default='codegen', help='The target stage for the compiler. It can be: scan, parse, ast, semantic, irt, codegen. The default is codegen.')
@click.option('--debug/--no-debug', default=False, help='List the stages you want to debug separating them with colons, p.e. scan:parse:irt')
@click.option('--out_name', '-o', help='Name for output file, p. e. \'my_file\'.')
def main(file_name, target, debug, out_name):
    click.echo("{}, {}, {}, {}".format(file_name, target, debug, out_name))
    token_stream = Scanner.scan(file_name, True)
    f = open(('outputs/' + str(out_name) + '.txt'), "a+")
    for tokenized in token_stream:
        line = str('\n\nlexeme: ' + str(tokenized.lexeme) + '\ntoken: ' + str(tokenized.token) + '\ntype: ' + tokenized.token_type + '\nline_num: ' + str(tokenized.line_num))
        f.write(line)
    f.close()


if __name__ == '__main__':
    main()
