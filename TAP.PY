import	ply.lex as lex
from utils import slurp
from treelib import Node, Tree


tokens = ('N_TESTS', 'OK_TEST', 'NOK_TEST', 'N_SUBTESTS', 'OK_SUBTEST', 'NOK_SUBTEST', 'COMMENT')

t_ignore = "\n"

resultTree = Tree()
node_root = resultTree.create_node(tag = "Root", identifier= "root")

def getNivel(s):
    return int((len(s) - len(s.lstrip()))/4)

def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT(t):
    r"-\s.*"
    t.value = t.value.replace("- ","")
    return t

def t_N_TESTS(t):
    r"[0-9]\.\.[0-9]+"
    global n_tests 
    n_tests += int(t.value[3:])
    return t

def t_N_SUBTESTS(t):
    r"\s[0-9]\.\.[0-9]+"
    global n_subtests 
    n_subtests += int(t.value.strip()[3:])
    return t

def t_OK_TEST(t):
    r"(ok)\s[0-9]+\s"
    global n_ok_tests
    global nodes, node, tree_aux
    nodes = [None] * 100

    if tree_aux != None:
        node = resultTree.create_node(t.value, t.value, parent= node_root, data = Tests(1, 0, "OK", t.value))
        resultTree.merge(t.value, tree_aux)
    else:
        resultTree.create_node(t.value, t.value, parent= node_root, data = Tests(1, 0, "OK", t.value)) 
    n_ok_tests += 1
    return t

def t_OK_SUBTEST(t):
    r"\s+(ok)\s[0-9]+\s"
    global n_ok_subtests, tree_aux
    n_ok_subtests += 1
    node = None
    n = getNivel(t.value) 
    if n == 1:
        if tree_aux != None:
            node = tree_aux.get_node("aux")
        if node == None:
            tree_aux = Tree()
            nodes[n-1] = tree_aux.create_node("aux", "aux", data = Tests(1, 0, "OK", "aux"))
    nodes[n] = tree_aux.create_node(t.value, t.value, parent=nodes[n-1], data = Tests(1, 0, "OK", t.value)) 
    return t

def t_NOK_TEST(t):
    r"(not\sok)\s[0-9]+"
    global n_nok_tests
    n_nok_tests += 1
    return t

def t_NOK_SUBTEST(t):
    r"\s+(not\sok)\s[0-9]+"
    global n_nok_subtests
    n_nok_subtests += 1
    return t    

lexer = lex.lex()

lexer.input(slurp("inputs/teste4.t"))