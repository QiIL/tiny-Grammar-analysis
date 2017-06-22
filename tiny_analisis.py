# -*- coding: UTF-8 -*-
import re
from tree import Tree


TINY_PROGRAME = re.compile(r'[A-Za-z0-9_][A-Za-z0-9_]*|\+|-|\*|/|<|>|:=|=|;|\(|\)|\[|\]|\{|\}|\$|~|`|!|@|#|%|\^|&|,|\?|\|')
OPERATOR = re.compile(r'\+|-|\*|/|<|>|:=|=|;|\{|\}')
NUMBER = re.compile(r'[0-9]+')
IDENTIFIER = re.compile(r'^[A-Za-z_][A-Za-z0-9_\]]*$')

class TAS():

    def __init__(self, file_con):
        self.articleCon = file_con
        self.tokengenarator = self.getToken()
        self.token = self.nextToken()
        self.error_message = []
        self.grammar_tree = self.programe()
        self.tree_line = []
        self.tree_node = []

    def output(self):
        print TINY_PROGRAME.findall(self.articleCon)
        if self.error_message:
            print self.error_message[0]
            return False
        else:
            self.grammar_tree.output_tree(self.grammar_tree, 0)
            return True

    def return_tree(self):
        return self.grammar_tree

    def Error(self):
        buf = str(self.token) + ' : not the expressed token'
        self.error_message.append(buf)

    def getToken(self):
        this_token = TINY_PROGRAME.findall(self.articleCon)
        this_token.append('$')
        for token in this_token:
            yield token

    def nextToken(self):
        try:
            token = next(self.tokengenarator)
            return token
        except StopIteration:
            return False

    def match(self, exprectedToken):
        if exprectedToken == self.token:
            #print exprectedToken
            self.token = self.nextToken()
        else:
            self.Error()
            self.token = self.nextToken()
        if not self.token:
            print 'done'

    def programe(self):
        temp = self.stmt_sequence()
        print 'end programe'
        return temp

    def stmt_sequence(self):
        temp = self.statement()
        while self.token == ';':
            newtemp = Tree('stmt-sequence')
            self.match(self.token)
            newtemp.child.append(temp)
            if self.token == 'else' or self.token == 'end' or self.token == '$' or self.token == 'endwhile' or self.token == 'enddo':
                break
            newtemp.child.append(self.statement())
            temp = newtemp
        if self.token == '$':
            newtemp = Tree('begin-programe')
            self.match(self.token)
            newtemp.child.append(temp)
            temp = newtemp
        print 'end stmt_sequence'
        return temp

    def statement(self):
        print self.token, 'statement token'
        if self.token == 'for':
            temp = self.for_stmt()
        elif self.token == 'repeat':
            temp = self.repeat_stmt()
        elif self.token == 'write':
            temp = self.write_stmt()
        elif self.token == 'read':
            temp = self.read_stmt()
        elif self.token == 'if':
            temp = self.if_stmt()
        elif self.token == 'do':
            temp = self.dowhile_stmt()
        elif self.token == 'while':
            temp = self.while_stmt()
        elif self.token == 'return':
            temp = self.return_stmt()
        elif IDENTIFIER.match(self.token):
            temp = self.assing_stmt()
        else:
            self.Error()
        print 'end statement'
        return temp

    def for_stmt(self):
        print self.token, 'in for stmt'
        temp = Tree('for')
        self.match('for')
        if IDENTIFIER.match(self.token):
            temp.child.append(self.token)
            self.match(self.token)
        else:
            self.Error()
        self.match(':=')
        temp.child.append(':=')
        temp.child.append(self.simple_exp())
        if self.token == 'to' or self.token == 'downto':
            temp.child.append(self.token)
            self.match(self.token)
        temp.child.append(self.simple_exp())
        self.match('do')
        temp.child.append('do')
        temp.child.append(self.stmt_sequence())
        self.match('enddo')
        temp.child.append('enddo')
        print 'end for_stmt'
        return temp

    def if_stmt(self):
        print self.token, 'in if stmt'
        self.match('if')
        temp = Tree('if')
        temp.child.append(self.exp())
        self.match('then')
        temp.child.append('then')
        temp.child.append(self.stmt_sequence())
        if self.token == 'else':
            self.match('else')
            temp.child.append('else')
            temp.child.append(self.stmt_sequence())
        self.match('end')
        temp.child.append('end')
        print 'end if_stmt'
        return temp

    def repeat_stmt(self):
        print self.token, 'in repeat stmt'
        temp = Tree('repeat')
        self.match('repeat')
        temp.child.append(self.stmt_sequence())
        temp.child.append('until')
        self.match('until')
        temp.child.append(self.exp())
        print 'end repeat_stmt'
        return temp

    def assing_stmt(self):
        print self.token, 'in assing stmt'
        temp = Tree('assing-stmt')
        temp.child.append(self.token)
        self.match(self.token)
        temp.child.append(':=')
        self.match(':=')
        temp.child.append(self.exp())
        print 'end assing_stmt'
        return temp

    def read_stmt(self):
        print self.token, 'in read stmt'
        temp = Tree('read')
        self.match('read')
        if IDENTIFIER.match(self.token):
            temp.child.append(self.token)
            self.match(self.token)
        else:
            self.Error()
        print 'end read_stmt'
        return temp

    def write_stmt(self):
        print self.token, 'in write stmt'
        temp = Tree('write')
        self.match('write')
        temp.child.append(self.exp())
        print 'end write_stmt'
        return temp

    def while_stmt(self):
        print self.token, 'in while stmt'
        temp = Tree('while-stmt')
        self.match('while')
        temp.child.append('while')
        temp.child.append(self.exp())
        self.match('do')
        temp.child.append('do')
        temp.child.append(self.stmt_sequence())
        self.match('endwhile')
        temp.child.append('endwhile')
        print 'end while_stmt'
        return temp

    def dowhile_stmt(self):
        print self.token, 'in do while stmt'
        temp = Tree('dowhile-stmt')
        self.match('do')
        temp.child.append('do')
        temp.child.append(self.stmt_sequence())
        self.match('while')
        temp.child.append('while')
        temp.child.append(self.exp())
        print 'end dowhile_stmt'
        return temp

    def return_stmt(self):
        print self.token, 'in return stmt'
        temp = Tree('return')
        self.match('return')
        temp.child.append(self.simple_exp())
        print 'end return_stmt'
        return temp

    def exp(self):
        temp = self.simple_exp()
        while self.token == '=' or self.token == '<':
            newtemp = Tree(self.token)
            self.match(self.token)
            newtemp.child.append(temp)
            newtemp.child.append(self.simple_exp())
            temp = newtemp
        print 'end exp'
        return temp

    def simple_exp(self):
        temp = self.term()
        while self.token == '+' or self.token == '-':
            newtemp = Tree(self.token)
            self.match(self.token)
            newtemp.child.append(temp)
            newtemp.child.append(self.term())
            temp = newtemp
        print 'end_simple_exp'
        return temp

    def term(self):
        temp = self.factor()
        while self.token == '*' or self.token == '/':
            newtemp = Tree(self.token)
            self.match(self.token)
            newtemp.child.append(temp)
            newtemp.child.append(self.factor())
            temp = newtemp
        print 'end term'
        return temp

    def factor(self):
        print self.token
        if self.token == '(':
            self.match('(')
            temp = Tree(self.exp())
            self.match(')')
            return temp
        elif NUMBER.match(self.token):
            temp = Tree(self.token)
            self.match(self.token)
            return temp
        elif self.token == 'random':
            buf = ''
            while self.token != ')':
                buf = buf + self.token
                self.match(self.token)
            self.match(self.token)
            temp = Tree(buf+')')
            return temp
        elif IDENTIFIER.match(self.token):
            buf = self.token
            self.match(self.token)
            if self.token == '[':
                cal_left_parenthesis = 1
                buf = buf + self.token
                self.match(self.token)
                while cal_left_parenthesis != 0:
                    buf = buf + self.token
                    if self.token == '[':
                        cal_left_parenthesis = cal_left_parenthesis + 1
                    elif self.token == ']':
                        cal_left_parenthesis = cal_left_parenthesis - 1
                    self.match(self.token)
            temp = Tree(buf)
            return temp
        elif self.token == '[':
            cal_left_parenthesis = 1
            buf = '['
            self.match(self.token)
            while cal_left_parenthesis != 0:
                buf = buf + self.token
                if self.token == '[':
                    cal_left_parenthesis = cal_left_parenthesis + 1
                elif self.token == ']':
                    cal_left_parenthesis = cal_left_parenthesis - 1
                self.match(self.token)
            temp = Tree(buf)
            return temp
        else:
            self.Error()

        print 'end factor'

