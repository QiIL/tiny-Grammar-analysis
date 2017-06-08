### Tiny 语言的递归下降分析程序
目标：根据Tiny的语法规则来编写递归下降的分析程序。

Tiny语言的文法规则如下：

``` C
$ program -> stmt-sequence
$ stmt-sequence -> statement {; statement}
$ statement -> if-stmt | repeat-stmt | assign-stmt | read-stmt | write-stmt
$ While-stmt --> while  exp  do  stmt-sequence  endwhile
Dowhile-stmt-->do  stmt-sequence  while  exp 
$ for-stmt-->for identifier:=simple-exp  to  simple-exp  do  stmt-sequence enddo    步长递增1
$ for-stmt-->for identifier:=simple-exp  downto  simple-exp  do  stmt-sequence enddo    步长递减1
$ if-stmt -> if exp then stmt-sequence [else stmt-sequence] end
$ repeat-stmt -> repeat stmt-sequence until exp
$ assign-stmt -> identifier := exp
$ read-stmt -> read identifier
$ write-stmt -> write exp
$ exp -> simple-exp [comparison-op simple-exp]
$ comparison-op -> < | =
$ simple-exp -> term {addop term}
$ adddop -> + | -
$ term -> factor {mulop factor}
$ mulop -> * | /
$ factor -> ( exp ) | number | identifier
```

### 运行

```python
$ python analisy_gui.py
```