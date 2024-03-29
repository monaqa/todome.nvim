" Save context
let s:save_cpo = &cpo
set cpo&vim

set nrformats=alpha

highlight default link TodomeOverdue Error
highlight default link TodomeDueToday IncSearch


" Folding {{{1
setlocal foldmethod=expr
setlocal foldexpr=TodoFoldLevel(v:lnum)
setlocal foldtext=TodoFoldText()

function! TodoFoldLevel(lnum)
    " The match function returns the index of the matching pattern or -1 if
    " the pattern doesn't match. In this case, we always try to match a
    " completed task from the beginning of the line so that the matching
    " function will always return -1 if the pattern doesn't match or 0 if the
    " pattern matches. Incrementing by one the value returned by the matching
    " function we will return 1 for the completed tasks (they will be at the
    " first folding level) while for the other lines 0 will be returned,
    " indicating that they do not fold.
    return match(getline(a:lnum),'^[xX]\s.\+$') + 1
endfunction

function! TodoFoldText()
    " The text displayed at the fold is formatted as '+- N Completed tasks'
    " where N is the number of lines folded.
    return '+' . v:folddashes . ' '
                \ . (v:foldend - v:foldstart + 1)
                \ . ' Completed tasks '
endfunction
" }}}

" Restore context
let &cpo = s:save_cpo
" Modeline
" vim: ts=2 sw=2
