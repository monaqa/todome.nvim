" File:        todome.nvim
" Description: Todo.txt syntax settings
" Author:      monaqa <mogassy@yahoo.co.jp>
" License:     Vim license
" Website:     http://github.com/mogassy/todome.nvim
" Version:     0.0.1

if exists("b:current_syntax")
    finish
endif

syntax  match  TodoDone       '^x\s.\+$'                     contains=TodoKey,TodoProject,TodoContext
syntax  match  TodoPriorityA  '^(A)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityB  '^(B)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityC  '^(C)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityD  '^(D)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityE  '^(E)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityF  '^(F)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityG  '^(G)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityH  '^(H)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityI  '^(I)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityJ  '^(J)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityK  '^(K)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityL  '^(L)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityM  '^(M)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityN  '^(N)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityO  '^(O)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityP  '^(P)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityQ  '^(Q)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityR  '^(R)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityS  '^(S)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityT  '^(T)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityU  '^(U)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityV  '^(V)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityW  '^(W)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityX  '^(X)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityY  '^(Y)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoPriorityZ  '^(Z)\s.\+$'                   contains=TodoKey,TodoDate,TodoProject,TodoContext,TodoDue
syntax  match  TodoDate       '\d\{2,4\}-\d\{2\}-\d\{2\}'       contains=NONE
syntax  match  TodoDue        '<\d\{2,4\}-\d\{2\}-\d\{2\}>'     contains=NONE
syntax  match  TodoKey        '\S*\S:\S\S*'                     contains=TodoDate
syntax  match  TodoProject    '\(^\|\W\)+[^[:blank:]]\+'        contains=NONE
syntax  match  TodoContext    '\(^\|\W\)@[^[:blank:]]\+'        contains=NONE
syntax  match  TodoComment    '^#.*'                            contains=NONE

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
highlight  default  link  TodoComment    Comment

let b:current_syntax = "todo"
