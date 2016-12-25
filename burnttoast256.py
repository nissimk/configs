# -*- coding: utf-8 -*-
"""
    Burnttoast256 Colorscheme
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

class Burnttoast256Style(Style):

    background_color = '#000000'
    styles = {
        Token:              'noinherit #d0d0d0 bg:#000000',
        Comment:            '#00af87',
        Generic.Error:      '#ffffff bg:#cd0000',
        Name.Entity:        '#d78787',
        String:             '#ffafaf',
        Keyword:            'noinherit #5fafff',
        Generic.Inserted:   'bg:#afd7af',
        Name.Tag:           'noinherit #5fafff',
        Number:             '#d7af87',
        Generic.Traceback:  '#ffffff bg:#cd0000',
        Name.Variable:      'noinherit #af5fd7',
        Generic.Deleted:    'noinherit bg:#949494',
        Keyword.Type:       'noinherit #afafd7',
        Name.Constant:      '#ffff5f',
        Generic.Emph:       '#00afff underline',
        Generic.Output:     '#3a3a3a',
        Comment.Preproc:    '#afd787',
    }
