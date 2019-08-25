" File:        todome.nvim
" Description: Todo.txt syntax settings
" Author:      monaqa <mogassy@yahoo.co.jp>
" License:     Vim license
" Website:     http://github.com/mogassy/todome.nvim
" Version:     0.0.1

if exists("b:current_syntax")
    finish
endif

syntax  match  TodoDone       '^[xX]\s.\+$'                     contains=TodoKey,TodoProject,TodoContext
syntax  match  TodoPriorityA  '^([aA])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityB  '^([bB])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityC  '^([cC])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityD  '^([dD])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityE  '^([eE])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityF  '^([fF])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityG  '^([gG])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityH  '^([hH])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityI  '^([iI])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityJ  '^([jJ])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityK  '^([kK])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityL  '^([lL])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityM  '^([mM])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityN  '^([nN])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityO  '^([oO])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityP  '^([pP])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityQ  '^([qQ])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityR  '^([rR])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityS  '^([sS])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityT  '^([tT])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityU  '^([uU])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityV  '^([vV])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityW  '^([wW])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityX  '^([xX])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityY  '^([yY])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityZ  '^([zZ])\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoDate       '\d\{2,4\}-\d\{2\}-\d\{2\}'       contains=NONE
syntax  match  TodoDue        '<\d\{2,4\}-\d\{2\}-\d\{2\}>'     contains=NONE
syntax  match  TodoKey        '\S*\S:\S\S*'                     contains=TodoDate
syntax  match  TodoProject    '\(^\|\W\)+[^[:blank:]]\+'        contains=NONE
syntax  match  TodoContext    '\(^\|\W\)@[^[:blank:]]\+'        contains=NONE

" Other priority colours might be defined by the user
highlight  default  link  TodoKey        Special
highlight  default  link  TodoDone       Comment
highlight  default  link  TodoPriorityA  Identifier
highlight  default  link  TodoPriorityB  statement
highlight  default  link  TodoPriorityC  type
highlight  default  link  TodoDate       PreProc
highlight  default  link  TodoDue        Constant
highlight  default  link  TodoProject    Special
highlight  default  link  TodoContext    Special

let b:current_syntax = "todo"
