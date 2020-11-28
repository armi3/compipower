# Usage
1. First get the venv up and running from the project's root directory.
```
source venv/bin/activate
```

2. Make sure you're working inside the (venv) and install all the dependencies.
```
pip install -r requirements.txt
```

3.  Now you're ready to run the compiler.
```
python Compiler.py examples/example5.dcf -t parse -o ex5
```
Replace `examples/example5.dcf` with the path to the decaf code you wish to compile (you can use one from the `\examples` directory or a file from your own).

The option `--target` or `-t` receives one of the six possible compiling stages as its argument (`scan`, `parse`, `ast`, `semantic`, `irt`, or `codegen`). If no option is specified, the compiler will execute until `codegen`, the default and final stage.

There are more options you can use, such as  `--out_name` (short is `-o`) and `--debug`. 
For more information on options available and their arguments use `--help`.
```
python Compiler.py --help
```

# Outputs
Check the `/outputs` directory to find the compiler's outputs, which are three.
### 🗒 Token stream to text
After tokenizing, the token stream is saved to `/outputs/output_name.txt`. 


### 🌳 Decorated AST to a PNG visualization
After parsing, the semantic analyzer flattens and reorganizes the AST until it's fit for type checking and passing to the IRT. 
This decorated AST is represented with a graph in `/outputs/graph.png`. 
![AST visualization](https://i.imgur.com/PEr6o3S.png)


### 📝 Symbol Table to an HTML table
After semantic analysis a symbol table is built and can be visualized in `/outputs/table.html` using any browser.
