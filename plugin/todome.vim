

autocmd FileType todo call s:todome_mapping()
function! s:todome_mapping() abort
  nnoremap <buffer> <leader>d i<C-r>=strftime("%Y-%m-%d")<CR><Space><Esc>
  inoremap <buffer> <C-t> <C-r>=strftime("%Y-%m-%d")<CR>
  nnoremap <buffer> <leader>x :call TodomeToggleDone()<CR>
  nnoremap <buffer> <leader>a :call TodomeAddPriority('A')<CR>
  nnoremap <buffer> <leader>b :call TodomeAddPriority('B')<CR>
  nnoremap <buffer> <leader>c :call TodomeAddPriority('C')<CR>
  nnoremap <buffer> <leader>d :call TodomeAddPriority('D')<CR>
endfunction
