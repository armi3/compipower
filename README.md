# Usage
1. First get the venv up and running from the project's root directory.
```
source venv/bin/activate
```
2. Run the configuration por use the CLI 
```
pip install --editable .
```

3. Making sure you're now working inside the (venv), run the compiler.
```
compiler examples/example2.dcf --target=scan -o 'ex2'
```
Replace `examples/example2.dcf` with the path to the decaf code you wish to compile (you can use one from the `\examples` directory or a file from your own).

The option `--target` or `-t` receives one of the six possible compiling stages as its argument (`scan`, `parse`, `ast`, `semantic`, `irt`, or `codegen`). If no option is specified, the compiler will execute until `codegen`, the default and final stage.

There are more options you can use, such as  `--out_name` (short is `-o`) and `--debug`. 
For more information on options available and their arguments use `--help`.
```
compiler --help
```
