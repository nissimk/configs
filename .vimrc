set nocompatible

filetype off
set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

Bundle 'gmarik/vundle'
Bundle "wookiehangover/jshint.vim"

call vundle#end()
filetype plugin indent on

syn on
colorscheme burnttoast256
set tabstop=4
set shiftwidth=4
set expandtab
set guifont=Monospace\ 8
set expandtab
set autoindent
set hidden
set pastetoggle=<F10>
set nu
set nocompatible

nnoremap <C-n> :bnext<CR>
nnoremap <C-p> :bprevious<CR>
nnoremap <Esc>n :bnext<CR>:redraw<CR>:ls<CR>
nnoremap <Esc>p :bprevious<CR>:redraw<CR>:ls<CR>
