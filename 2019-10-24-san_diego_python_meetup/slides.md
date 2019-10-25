%title: PFP - Python Format Parser
%author: James Johnson
%date: 2019-10-24

-> # Me <-

* James Johnson
* Career is a mix between security research, software dev, devops, IT
* ~12 years programming
* ~10 years computer security

* Running the engineering team at a Carlsbad-based cyber security
  startup

--------------------------------------------------

-> # Hiring <-

* Sr DevOps Engineer

--------------------------------------------------

-> # Joke <-

Interviewer: "I heard you were extremely quick at math"

Me: "yes, as a matter of fact I am"

Interviewer: "Whats 14x27"

Me: "49"

Interviewer: "that's not even close"

me: "yeah, but it was fast"

  - Reddit
    - Micheal Scott

--------------------------------------------------

-> # PFP - 010 Editor Template Interpreter <-

* Parses data

* Is an interpreter for [010](https://www.sweetscape.com/010editor/) [templates](https://www.sweetscape.com/010editor/repository/templates/)

* Generates a Document Object Model (DOM) from the parsed data

* Able to traverse DOM and edit fields

* Rebuilds modified parsed data

--------------------------------------------------

-> # PFP - Origins

This iteration of pfp created in 2015:

```
commit 2d6f1aa9d4f492d0aa9cdf27ef5d28150863d5de
Author: James Johnson <d0c.s4vage@gmail.com>
Date:   Thu Mar 26 05:27:06 2015 -0500
 
    Initial commit
```

--------------------------------------------------

-> # PFP - Structure

* Is composed of two projects:
  * [py010parser](https://github.com/d0c-s4vage/py010parser) - A modified version of pycparser
  * [pfp](https://github.com/d0c-s4vage/pfp) - The interpreter

--------------------------------------------------

-> # PFP - Size

pfp project alone is decent sized, with over 400 tests:

```
$> find pfp -iname "*.py" -exec cat {} \; | wc -l
9870
$> find tests -iname "*.py" -exec cat {} \; | wc -l
4502
```

--------------------------------------------------

-> # PFP - Installation <-



```
pip install pfp
```

--------------------------------------------------

-> # 010 Templates <-

* Are interpreted scripts

* Use a modified C syntax

* Parse values from the input stream by declaring variables

--------------------------------------------------

-> # 010 Templates: Example <-

```
BigEndian();
 
typedef struct {
    uint32 length;
    char type[4];
    char data[length];
    uint32 crc;
} PngChunk;
 
struct {
    uchar signature[8];
 
    while (!FEof()) {
        PngChunk chunks;
    }
} PNG;
```

010 Editor Demo Time!

--------------------------------------------------

-> # PFP Example: Console Script <-

Using the pfp command-line:

```
pfp -t png_basic.bt python.png
```

--------------------------------------------------

-> # PFP Example: Python Code <-

A python script:

```
import pfp
 
template = """
BigEndian();
 
typedef struct {
    uint32 length;
    char type[4];
    char data[length];
    uint32 crc;
} PngChunk;
 
struct {
    uchar signature[8];
 
    while (!FEof()) {
        PngChunk chunks;
    }
} PNG;
"""
 
dom = pfp.parse(data_file="python.png", template=template)
print(dom._pfp__show())
```

--------------------------------------------------

-> # Py010Parser: Lexer & Yacc <-

* lexer - tokenizes input into distinct tokens

* YACC - "Yet Another Compiler Compiler"
  * Implements the rules of the *GRAMMAR*

--------------------------------------------------

-> # Py010Parser: Lexer I <-

* lexer - tokenizes input into distinct tokens

*py010parser/c_lexer.py*

```
    ##
    ## All the tokens recognized by the lexer
    ##
    tokens = keywords + (
        # Identifiers
        'ID',
 
        # for parameterized structs
        'STRUCT_CALL',
 
        # Type identifiers (identifiers previously defined as
        # types with typedef)
        'TYPEID',
 
        # constants
        'INT_CONST_DEC', 'INT_CONST_OCT', 'INT_CONST_HEX',
        'FLOAT_CONST', 'HEX_FLOAT_CONST',
        'CHAR_CONST',
        'WCHAR_CONST',
 
        # String literals
        'STRING_LITERAL',
        'WSTRING_LITERAL',
 
        # ...
    )
```

--------------------------------------------------

-> # Py010Parser: Lexer II <-

* lexer - tokenizes input into distinct tokens

*py010parser/c_lexer.py*

```
    # valid C identifiers (K&R2: A.2.3), plus '$' (supported by some compilers)
    identifier = r'[a-zA-Z_$][0-9a-zA-Z_$]*'
```

--------------------------------------------------

-> # Py010Parser: YACC <-

Yacc consumes the token stream produced by the lexer and applies its grammar
rules:

*py010parser/c_parser.py*

```
def p_unary_expression_3(self, p):
    """ unary_expression    : SIZEOF unary_expression
                            | SIZEOF LPAREN type_name RPAREN
                            | EXISTS unary_expression
                            | EXISTS LPAREN type_name RPAREN
                            | FUNCTION_EXISTS unary_expression
                            | FUNCTION_EXISTS LPAREN type_name RPAREN
                            | PARENTOF unary_expression
                            | PARENTOF LPAREN type_name RPAREN
                            | STARTOF unary_expression
                            | STARTOF LPAREN type_name RPAREN
    """
    # ...
```

--------------------------------------------------

-> # Pfp: Interpreter I <-

Pfp is an *interpreter*:

* Consumes the AST produced by py010parser's yacc
* Holds data structures, state, and context in-memory as the AST is traversed

--------------------------------------------------

-> # Pfp: Interpreter II <-

Pfp is an *interpreter*.

A few functions that handle specific node types within the AST:

```
   +_handle_binary_op : function
   +_handle_break : function
   +_handle_byref_decl : function
   +_handle_cast : function
   +_handle_compound : function
   +_handle_constant : function
   +_handle_continue : function
   +_handle_decl : function
   +_handle_decl_list : function
   +_handle_do_while : function
   +_handle_empty_statement : function
   +_handle_enum : function
   +_handle_exists : function
   +_handle_expr_list : function
   +_handle_file_ast : function
   +_handle_for : function
   +_handle_func_call : function
```

--------------------------------------------------

-> # Pfp: Debugger <-

Pfp contains a debugger for interactive debugging of 010 templates. This uses
the builtin `cmd.Cmd` class:

*pfp/dbg.py*

```
class PfpDbg(cmd.Cmd, object):
    """The pfp debugger cmd.Cmd class"""
 
    prompt = "pfp> "
```

--------------------------------------------------

-> # Pfp: Debugger <-

The debugger may be triggered directly from an 010 template with the built-in
*Int3()* function.

Demo Time!

--------------------------------------------------

-> # Pfp: Fuzzing <-


Pfp was made to help with common security research tasks:

* Reverse engineering

* Fuzzing

--------------------------------------------------

-> # Pfp: Fuzzing PNGs <-

Simple example of fuzzing all integer-based fields within a
PNG:

Demo Time!

--------------------------------------------------

-> # Pfp: Vim Plugin! <-

I also wrote a vim plugin to display data structures parsed by pfp:

  [pfp-vim](https://github.com/d0c-s4vage/pfp-vim)

Demo Time!
