
###### AndroidManifestTemplate.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cLtGreen' at <string>:124

###### AVITemplate.bt ######
    File "pfp/pfp/native/compat_string.py", line 117, in Memcmp
      raise NotImplementedError()

###### BMPTemplate.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cLtGray' at <string>:51

###### CABTemplate.bt ######
      File "pfp/pfp/interp.py", line 687, in parse
        res = self._run(keep_successful)
      File "pfp/pfp/interp.py", line 884, in _run
        traceback
      File "pfp/pfp/interp.py", line 863, in _run
        res = self._handle_node(self._ast, None, None, self._stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 979, in _handle_file_ast
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2129, in _handle_while
        self._handle_node(node.stmt, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1960, in _handle_compound
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1170, in _handle_decl
        field._pfp__init(stream)
      File "pfp/pfp/interp.py", line 81, in _pfp__init
        stream=stream
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1472, in _handle_struct_decls
        self._handle_node(decl, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1143, in _handle_decl
        bitfield_left_right=bitfield_left_right
      File "pfp/pfp/fields.py", line 985, in __init__
        super(NumberBase, self).__init__(stream, metadata_processor=metadata_processor)
      File "pfp/pfp/fields.py", line 231, in __init__
        self._pfp__parse(stream, save_offset=True)
      File "pfp/pfp/fields.py", line 1023, in _pfp__parse
        raise errors.PrematureEOF()

###### CAPTemplate.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'false' at <string>:778

###### CDATemplate.bt ######
works

###### CLASSTemplate.bt ######
works

###### CLASSTemplate2.bt ######
      File "pfp/pfp/interp.py", line 687, in parse
        res = self._run(keep_successful)
      File "pfp/pfp/interp.py", line 884, in _run
        traceback
      File "pfp/pfp/interp.py", line 863, in _run
        res = self._handle_node(self._ast, None, None, self._stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 979, in _handle_file_ast
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1170, in _handle_decl
        field._pfp__init(stream)
      File "pfp/pfp/interp.py", line 81, in _pfp__init
        stream=stream
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1472, in _handle_struct_decls
        self._handle_node(decl, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2102, in _handle_for
        self._handle_node(node.stmt, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1960, in _handle_compound
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1170, in _handle_decl
        field._pfp__init(stream)
      File "pfp/pfp/interp.py", line 81, in _pfp__init
        stream=stream
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1472, in _handle_struct_decls
        self._handle_node(decl, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1143, in _handle_decl
        bitfield_left_right=bitfield_left_right
      File "pfp/pfp/fields.py", line 985, in __init__
        super(NumberBase, self).__init__(stream, metadata_processor=metadata_processor)
      File "pfp/pfp/fields.py", line 231, in __init__
        self._pfp__parse(stream, save_offset=True)
      File "pfp/pfp/fields.py", line 1023, in _pfp__parse
        raise errors.PrematureEOF()

###### CLASSTemplate3.bt ######
      File "pfp/pfp/interp.py", line 278, in level
        res += self._parent.level()
      File "pfp/pfp/interp.py", line 273, in level
        def level(self):
    pfp.errors.PfpError: RuntimeError: maximum recursion depth exceeded

###### CRXTemplate.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cNone' at <string>:134

###### DBFTemplate.bt ######
      File "pfp/pfp/interp.py", line 687, in parse
        res = self._run(keep_successful)
      File "pfp/pfp/interp.py", line 884, in _run
        traceback
      File "pfp/pfp/interp.py", line 863, in _run
        res = self._handle_node(self._ast, None, None, self._stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 979, in _handle_file_ast
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1170, in _handle_decl
        field._pfp__init(stream)
      File "pfp/pfp/interp.py", line 81, in _pfp__init
        stream=stream
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1472, in _handle_struct_decls
        self._handle_node(decl, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1064, in _handle_decl
        field = self._handle_node(node.type, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2038, in _handle_array_decl
        array_size = self._handle_node(node.dim, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1630, in _handle_binary_op
        right_val = self._handle_node(node.right, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1686, in _handle_unary_op
        res = switch[node.op](field, 1)
      File "pfp/pfp/interp.py", line 1675, in <lambda>
        "sizeof":	lambda x,v: (fields.UInt64()+x._pfp__width()),
    pfp.errors.PfpError: AttributeError: 'NoneType' object has no attribute '_pfp__width'

###### DEXTemplate.bt ######
###### DEXTemplate.new.bt ######
works

###### DMPTemplate.bt ######
not tested

###### EDIDTemplate.bt ######
      File "pfp/pfp/interp.py", line 684, in parse
        self._ast = self._parse_string(template, predefines)
      File "pfp/pfp/interp.py", line 828, in _parse_string
        keep_scopes=predefines
      File "py010parser/py010parser/__init__.py", line 90, in parse_string
        keep_scopes     = keep_scopes
      File "py010parser/py010parser/c_parser.py", line 178, in parse
        debug=debuglevel)
      File "py010parser/py010parser/ply/yacc.py", line 265, in parse
        return self.parseopt_notrack(input,lexer,debug,tracking,tokenfunc)
      File "py010parser/py010parser/ply/yacc.py", line 1047, in parseopt_notrack
        tok = self.errorfunc(errtoken)
      File "py010parser/py010parser/c_parser.py", line 1952, in p_error
        column=self.clex.find_tok_column(p)))
      File "py010parser/py010parser/plyparser.py", line 54, in _parse_error
        raise ParseError("%s: %s" % (coord, msg))
    py010parser.plyparser.ParseError: <string>:566:55: before: =

###### ELFTemplate.bt ######
      File "pfp/pfp/interp.py", line 684, in parse
        self._ast = self._parse_string(template, predefines)
      File "pfp/pfp/interp.py", line 828, in _parse_string
        keep_scopes=predefines
      File "py010parser/py010parser/__init__.py", line 90, in parse_string
        keep_scopes     = keep_scopes
      File "py010parser/py010parser/c_parser.py", line 178, in parse
        debug=debuglevel)
      File "py010parser/py010parser/ply/yacc.py", line 265, in parse
        return self.parseopt_notrack(input,lexer,debug,tracking,tokenfunc)
      File "py010parser/py010parser/ply/yacc.py", line 1047, in parseopt_notrack
        tok = self.errorfunc(errtoken)
      File "py010parser/py010parser/c_parser.py", line 1952, in p_error
        column=self.clex.find_tok_column(p)))
      File "py010parser/py010parser/plyparser.py", line 54, in _parse_error
        raise ParseError("%s: %s" % (coord, msg))
    py010parser.plyparser.ParseError: <string>:353:24: before: char

###### EMFTemplate.bt ######
      File "pfp/pfp/interp.py", line 687, in parse
        res = self._run(keep_successful)
      File "pfp/pfp/interp.py", line 884, in _run
        traceback
      File "pfp/pfp/interp.py", line 863, in _run
        res = self._handle_node(self._ast, None, None, self._stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 979, in _handle_file_ast
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2150, in _handle_do_while
        self._handle_node(node.stmt, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1960, in _handle_compound
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1170, in _handle_decl
        field._pfp__init(stream)
      File "pfp/pfp/interp.py", line 81, in _pfp__init
        stream=stream
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1472, in _handle_struct_decls
        self._handle_node(decl, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1143, in _handle_decl
        bitfield_left_right=bitfield_left_right
      File "pfp/pfp/fields.py", line 1370, in __init__
        bitfield_left_right	= bitfield_left_right
      File "pfp/pfp/fields.py", line 985, in __init__
        super(NumberBase, self).__init__(stream, metadata_processor=metadata_processor)
      File "pfp/pfp/fields.py", line 231, in __init__
        self._pfp__parse(stream, save_offset=True)
      File "pfp/pfp/fields.py", line 1379, in _pfp__parse
        res = super(Enum, self)._pfp__parse(stream, save_offset)
      File "pfp/pfp/fields.py", line 1023, in _pfp__parse
        raise errors.PrematureEOF()

###### EOTTemplate.bt ######
###### EVSBTemplate.bt ######
not tested

###### EXETemplate.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cLtGray' at <string>:290

###### EXETemplate2.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'true' at <string>:308
-> https://github.com/d0c-s4vage/py010parser/issues/13

###### exFATTemplate.bt ######
      File "pfp/pfp/interp.py", line 1080, in _handle_decl
        and prev.bitsize is not None and prev.bitfield_rw.reserve_bits(bitsize, stream):
    pfp.errors.PfpError: AttributeError: 'Array_UChar_2' object has no attribute 'bitsize'

###### FAT16Template.bt ######
works

###### FLVTemplate.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cLtGray' at <string>:48

###### GeoTIFTemplate.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cLtRed' at <string>:1022

###### GIFTemplate.bt ######
works

###### GocleverTemplate.bt ######
      File "pfp/pfp/native/compat_string.py", line 388, in TimeTToString
        raise NotImplementedError()

###### GPTTemplate.bt ######
works

###### GZipTemplate.bt ######
works

###### ICOTemplate.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cNone' at <string>:119

###### InspectorDates.bt ######
###### InspectorWithMP4DateTime.bt ######
      File "pfp/pfp/functions.py", line 74, in call
        res = self.func(args, ctxt, scope, stream, coord)
      File "pfp/pfp/native/compat_interface.py", line 620, in RequiresVersion
        raise NotImplementedError()    

###### ISOBMFTemplate.bt ######
      File "pfp/pfp/interp.py", line 687, in parse
        res = self._run(keep_successful)
      File "pfp/pfp/interp.py", line 884, in _run
        traceback
      File "pfp/pfp/interp.py", line 863, in _run
        res = self._handle_node(self._ast, None, None, self._stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 979, in _handle_file_ast
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2129, in _handle_while
        self._handle_node(node.stmt, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1960, in _handle_compound
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1170, in _handle_decl
        field._pfp__init(stream)
      File "pfp/pfp/interp.py", line 81, in _pfp__init
        stream=stream
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1472, in _handle_struct_decls
        self._handle_node(decl, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2232, in _handle_switch
        if expr == cond:
      File "pfp/pfp/fields.py", line 534, in __eq__
        val = get_value(other)
      File "pfp/pfp/fields.py", line 31, in get_value
        return field._pfp__value
    pfp.errors.PfpError: AttributeError: 'Array_Char_4' object has no attribute '_pfp__value'

###### JPGTemplate.bt ######
      File "pfp/pfp/interp.py", line 687, in parse
        res = self._run(keep_successful)
      File "pfp/pfp/interp.py", line 884, in _run
        traceback
      File "pfp/pfp/interp.py", line 863, in _run
        res = self._handle_node(self._ast, None, None, self._stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 979, in _handle_file_ast
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1170, in _handle_decl
        field._pfp__init(stream)
      File "pfp/pfp/interp.py", line 81, in _pfp__init
        stream=stream
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1472, in _handle_struct_decls
        self._handle_node(decl, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2129, in _handle_while
        self._handle_node(node.stmt, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1960, in _handle_compound
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2234, in _handle_switch
        exec_case(idx, cases)
      File "pfp/pfp/interp.py", line 2183, in exec_case
        self._handle_node(stmt, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1170, in _handle_decl
        field._pfp__init(stream)
      File "pfp/pfp/interp.py", line 81, in _pfp__init
        stream=stream
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1472, in _handle_struct_decls
        self._handle_node(decl, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2078, in _handle_if
        return self._handle_node(node.iftrue, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1960, in _handle_compound
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2129, in _handle_while
        self._handle_node(node.stmt, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1960, in _handle_compound
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2075, in _handle_if
        cond = self._handle_node(node.cond, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1630, in _handle_binary_op
        right_val = self._handle_node(node.right, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1791, in _handle_id
        raise errors.UnresolvedID(node.coord, node.name)
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'DK_End' at <string>:1138

###### LNKTemplate.bt ######
pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cNone' at <string>:10

###### LUKSTemplate.bt ######
works

###### MachOTemplate.bt ######
py010parser.plyparser.ParseError: <string>:8: Directives not supported yet

###### MBRTemplate.bt ######
works

###### MBRTemplateFAT.bt ######
      File "pfp/pfp/interp.py", line 684, in parse
        self._ast = self._parse_string(template, predefines)
      File "pfp/pfp/interp.py", line 828, in _parse_string
        keep_scopes=predefines
      File "py010parser/py010parser/__init__.py", line 90, in parse_string
        keep_scopes     = keep_scopes
      File "py010parser/py010parser/c_parser.py", line 178, in parse
        debug=debuglevel)
      File "py010parser/py010parser/ply/yacc.py", line 265, in parse
        return self.parseopt_notrack(input,lexer,debug,tracking,tokenfunc)
      File "py010parser/py010parser/ply/yacc.py", line 1047, in parseopt_notrack
        tok = self.errorfunc(errtoken)
      File "py010parser/py010parser/c_parser.py", line 1952, in p_error
        column=self.clex.find_tok_column(p)))
      File "py010parser/py010parser/plyparser.py", line 54, in _parse_error
        raise ParseError("%s: %s" % (coord, msg))
    py010parser.plyparser.ParseError: <string>:763:1: before: /

###### MIDITemplate.bt ######
works

###### Mifare1kTemplate.bt ######
###### Mifare4kTemplate.bt ######
works

###### MOBITemplate.bt ######
      File "pfp/pfp/interp.py", line 684, in parse
        self._ast = self._parse_string(template, predefines)
      File "pfp/pfp/interp.py", line 828, in _parse_string
        keep_scopes=predefines
      File "py010parser/py010parser/__init__.py", line 90, in parse_string
        keep_scopes     = keep_scopes
      File "py010parser/py010parser/c_parser.py", line 178, in parse
        debug=debuglevel)
      File "py010parser/py010parser/ply/yacc.py", line 265, in parse
        return self.parseopt_notrack(input,lexer,debug,tracking,tokenfunc)
      File "py010parser/py010parser/ply/yacc.py", line 971, in parseopt_notrack
        p.callable(pslice)
      File "py010parser/py010parser/c_parser.py", line 752, in p_decl_body_1
        typedef_namespace=True)
      File "py010parser/py010parser/c_parser.py", line 567, in _build_declarations
        self._add_typedef_name(fixed_decl.name, fixed_decl.coord)
      File "py010parser/py010parser/c_parser.py", line 278, in _add_typedef_name
        "in this scope" % name, coord)
      File "py010parser/py010parser/plyparser.py", line 54, in _parse_error
        raise ParseError("%s: %s" % (coord, msg))
    py010parser.plyparser.ParseError: <string>:391: Typedef 'HTML' previously declared as non-typedef in this scope

###### MP3Template.bt ######
works

###### MP4Template.bt ######
      File "pfp/pfp/interp.py", line 684, in parse
        self._ast = self._parse_string(template, predefines)
      File "pfp/pfp/interp.py", line 828, in _parse_string
        keep_scopes=predefines
      File "py010parser/py010parser/__init__.py", line 90, in parse_string
        keep_scopes     = keep_scopes
      File "py010parser/py010parser/c_parser.py", line 178, in parse
        debug=debuglevel)
      File "py010parser/py010parser/ply/yacc.py", line 265, in parse
        return self.parseopt_notrack(input,lexer,debug,tracking,tokenfunc)
      File "py010parser/py010parser/ply/yacc.py", line 1047, in parseopt_notrack
        tok = self.errorfunc(errtoken)
      File "py010parser/py010parser/c_parser.py", line 1952, in p_error
        column=self.clex.find_tok_column(p)))
      File "py010parser/py010parser/plyparser.py", line 54, in _parse_error
        raise ParseError("%s: %s" % (coord, msg))
    py010parser.plyparser.ParseError: <string>:127:1: before: /

###### NetflowVersion5.bt ######
works

###### OGGTemplate.bt ######
unknown

###### OrCAD3.20a_LIB.bt ######
###### OrCad3.20a_SCH.bt ######
works

###### OscarItemTemplate.bt ######
no test data

###### PALTemplate.bt ######
works

###### PCAPTemplate.bt ######
      File "pfp/pfp/interp.py", line 687, in parse
        res = self._run(keep_successful)
      File "pfp/pfp/interp.py", line 884, in _run
        traceback
      File "pfp/pfp/interp.py", line 863, in _run
        res = self._handle_node(self._ast, None, None, self._stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 979, in _handle_file_ast
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2129, in _handle_while
        self._handle_node(node.stmt, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1960, in _handle_compound
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1170, in _handle_decl
        field._pfp__init(stream)
      File "pfp/pfp/interp.py", line 81, in _pfp__init
        stream=stream
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1472, in _handle_struct_decls
        self._handle_node(decl, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1064, in _handle_decl
        field = self._handle_node(node.type, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1427, in _handle_struct_call_type_decl
        struct_args = self._handle_node(node.args, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1941, in _handle_expr_list
        self._handle_node(expr, scope, ctxt, stream) for expr in node.exprs
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1346, in _handle_struct_ref
        sub_field = getattr(struct, node.field.name)
      File "pfp/pfp/fields.py", line 753, in __getattr__
        return super(Struct, self).__getattribute__(name)
    pfp.errors.PfpError: AttributeError: 'Layer_3_' object has no attribute 'L4proto'

###### PCXTemplate.bt ######
works

###### PDFTemplate.bt ######
      File "pfp/pfp/interp.py", line 684, in parse
        self._ast = self._parse_string(template, predefines)
      File "pfp/pfp/interp.py", line 828, in _parse_string
        keep_scopes=predefines
      File "py010parser/py010parser/__init__.py", line 90, in parse_string
        keep_scopes     = keep_scopes
      File "py010parser/py010parser/c_parser.py", line 178, in parse
        debug=debuglevel)
      File "py010parser/py010parser/ply/yacc.py", line 265, in parse
        return self.parseopt_notrack(input,lexer,debug,tracking,tokenfunc)
      File "py010parser/py010parser/ply/yacc.py", line 1047, in parseopt_notrack
        tok = self.errorfunc(errtoken)
      File "py010parser/py010parser/c_parser.py", line 1952, in p_error
        column=self.clex.find_tok_column(p)))
      File "py010parser/py010parser/plyparser.py", line 54, in _parse_error
        raise ParseError("%s: %s" % (coord, msg))
    py010parser.plyparser.ParseError: <string>:4:6: before: int

###### PETemplate.bt ######
    Error parsing with py010parser
      File "pfp/pfp/interp.py", line 684, in parse
        self._ast = self._parse_string(template, predefines)
      File "pfp/pfp/interp.py", line 828, in _parse_string
        keep_scopes=predefines
      File "py010parser/py010parser/__init__.py", line 90, in parse_string
        keep_scopes     = keep_scopes
      File "py010parser/py010parser/c_parser.py", line 178, in parse
        debug=debuglevel)
      File "py010parser/py010parser/ply/yacc.py", line 265, in parse
        return self.parseopt_notrack(input,lexer,debug,tracking,tokenfunc)
      File "py010parser/py010parser/ply/yacc.py", line 1047, in parseopt_notrack
        tok = self.errorfunc(errtoken)
      File "py010parser/py010parser/c_parser.py", line 1952, in p_error
        column=self.clex.find_tok_column(p)))
      File "py010parser/py010parser/plyparser.py", line 54, in _parse_error
        raise ParseError("%s: %s" % (coord, msg))
    py010parser.plyparser.ParseError: <string>:47:83: before: 2

###### PNG12Template.bt ######
      File "pfp/pfp/interp.py", line 687, in parse
        res = self._run(keep_successful)
      File "pfp/pfp/interp.py", line 884, in _run
        traceback
      File "pfp/pfp/interp.py", line 863, in _run
        res = self._handle_node(self._ast, None, None, self._stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 979, in _handle_file_ast
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1170, in _handle_decl
        field._pfp__init(stream)
      File "pfp/pfp/interp.py", line 81, in _pfp__init
        stream=stream
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1472, in _handle_struct_decls
        self._handle_node(decl, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1925, in _handle_func_call
        func_args = self._handle_node(node.args, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1941, in _handle_expr_list
        self._handle_node(expr, scope, ctxt, stream) for expr in node.exprs
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1791, in _handle_id
        raise errors.UnresolvedID(node.coord, node.name)
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cRed' at <string>:79

###### PNGTemplate.bt ######
      File "pfp/pfp/interp.py", line 687, in parse
        res = self._run(keep_successful)
      File "pfp/pfp/interp.py", line 884, in _run
        traceback
      File "pfp/pfp/interp.py", line 863, in _run
        res = self._handle_node(self._ast, None, None, self._stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 979, in _handle_file_ast
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2129, in _handle_while
        self._handle_node(node.stmt, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1960, in _handle_compound
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1170, in _handle_decl
        field._pfp__init(stream)
      File "pfp/pfp/interp.py", line 81, in _pfp__init
        stream=stream
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1472, in _handle_struct_decls
        self._handle_node(decl, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1104, in _handle_decl
        val = self._handle_node(node.init, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1925, in _handle_func_call
        func_args = self._handle_node(node.args, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1941, in _handle_expr_list
        self._handle_node(expr, scope, ctxt, stream) for expr in node.exprs
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1791, in _handle_id
        raise errors.UnresolvedID(node.coord, node.name)
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'CHECKSUM_CRC32' at <string>:52

###### PSFTemplate.bt ######
      File "pfp/pfp/interp.py", line 687, in parse
        res = self._run(keep_successful)
      File "pfp/pfp/interp.py", line 884, in _run
        traceback
      File "pfp/pfp/interp.py", line 863, in _run
        res = self._handle_node(self._ast, None, None, self._stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 979, in _handle_file_ast
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1858, in _handle_func_def
        func = self._handle_node(node.decl, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1064, in _handle_decl
        field = self._handle_node(node.type, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1901, in _handle_func_decl
        params = self._handle_node(node.args, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1877, in _handle_param_list
        param = self._handle_node(param, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1064, in _handle_decl
        field = self._handle_node(node.type, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1312, in _handle_byref_decl
        field.byref = True
    pfp.errors.PfpError: AttributeError: 'NoneType' object has no attribute 'byref'

###### PYCTemplate.bt ######
      File "pfp/pfp/native/compat_string.py", line 62, in EnumToString
        raise NotImplementedError()
  
###### RARTemplate.bt ######
      File "pfp/pfp/interp.py", line 1791, in _handle_id
        raise errors.UnresolvedID(node.coord, node.name)
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'CHECKSUM_CRC32' at <string>:180

###### RDBTemplate.bt ######
works

###### RegistryPolicyFileTemplate.bt ######
works

###### RESTemplate.bt ######
      File "pfp/pfp/interp.py", line 687, in parse
        res = self._run(keep_successful)
      File "pfp/pfp/interp.py", line 884, in _run
        traceback
      File "pfp/pfp/interp.py", line 863, in _run
        res = self._handle_node(self._ast, None, None, self._stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 979, in _handle_file_ast
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1926, in _handle_func_call
        func = self._handle_node(node.name, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1791, in _handle_id
        raise errors.UnresolvedID(node.coord, node.name)
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'GoTo_rsrc_section' at <string>:5

###### ROMFS.bt ######
      File "py010parser/py010parser/plyparser.py", line 54, in _parse_error
        raise ParseError("%s: %s" % (coord, msg))
    py010parser.plyparser.ParseError: <string>:7: Directives not supported yet

###### SHPTemplate.bt ######
      File "pfp/pfp/interp.py", line 1791, in _handle_id
        raise errors.UnresolvedID(node.coord, node.name)
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cLtGreen' at <string>:11

###### SHXTemplate.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cLtGreen' at <string>:11

###### SinclairMicrodriveImage.bt ######
no test data
    
###### SRecTemplate.bt ######
      File "pfp/pfp/interp.py", line 687, in parse
        res = self._run(keep_successful)
      File "pfp/pfp/interp.py", line 884, in _run
        traceback
      File "pfp/pfp/interp.py", line 863, in _run
        res = self._handle_node(self._ast, None, None, self._stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 979, in _handle_file_ast
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2129, in _handle_while
        self._handle_node(node.stmt, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1960, in _handle_compound
        self._handle_node(child, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1170, in _handle_decl
        field._pfp__init(stream)
      File "pfp/pfp/interp.py", line 81, in _pfp__init
        stream=stream
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 1472, in _handle_struct_decls
        self._handle_node(decl, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 956, in _handle_node
        res = self._node_switch[node.__class__](node, scope, ctxt, stream)
      File "pfp/pfp/interp.py", line 2232, in _handle_switch
        if expr == cond:
      File "pfp/pfp/fields.py", line 534, in __eq__
        val = get_value(other)
      File "pfp/pfp/fields.py", line 31, in get_value
        return field._pfp__value
    pfp.errors.PfpError: AttributeError: 'Array_Char_2' object has no attribute '_pfp__value'

###### SSPTemplate.bt ######
works

###### STLTemplate.bt ######
      File "pfp/pfp/interp.py", line 1791, in _handle_id
        raise errors.UnresolvedID(node.coord, node.name)
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cLtAqua' at <string>:33

###### SWFTemplate.bt ######
      File "pfp/pfp/interp.py", line 1791, in _handle_id
        raise errors.UnresolvedID(node.coord, node.name)
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cLtGray' at <string>:2055

###### TacxTemplate.bt ######
works

###### TGATemplate.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cLtGray' at <string>:105

###### TIFTemplate.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cLtAqua' at <string>:1017

###### TOCTemplate.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cGreen' at <string>:26

###### TTFTemplate.bt ######
      File "pfp/pfp/interp.py", line 684, in parse
        self._ast = self._parse_string(template, predefines)
      File "pfp/pfp/interp.py", line 828, in _parse_string
        keep_scopes=predefines
      File "py010parser/py010parser/__init__.py", line 90, in parse_string
        keep_scopes     = keep_scopes
      File "py010parser/py010parser/c_parser.py", line 178, in parse
        debug=debuglevel)
      File "py010parser/py010parser/ply/yacc.py", line 265, in parse
        return self.parseopt_notrack(input,lexer,debug,tracking,tokenfunc)
      File "py010parser/py010parser/ply/yacc.py", line 1047, in parseopt_notrack
        tok = self.errorfunc(errtoken)
      File "py010parser/py010parser/c_parser.py", line 1952, in p_error
        column=self.clex.find_tok_column(p)))
      File "py010parser/py010parser/plyparser.py", line 54, in _parse_error
        raise ParseError("%s: %s" % (coord, msg))
    py010parser.plyparser.ParseError: <string>:587:1: before: /

###### UTMPTemplate.bt ######
no test data

###### VHDTemplate.bt ######
    File "pfp/pfp/native/compat_string.py", line 117, in Memcmp
        raise NotImplementedError()

###### WAVTemplate.bt ######
###### WAVTemplateAdv.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'false' at <string>:4

###### WinhexPosTemplate.bt ######
no test data

###### WMFTemplate.bt ######
works

###### ZIPTemplate.bt ######
###### ZIPTemplateAdv.bt ######
    pfp.errors.PfpError: UnresolvedID: Could not resolve field 'cLtGray' at <string>:125
