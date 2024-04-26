


```

TENKA_OVERKILL

...she isn't perfect. but if you know some emacs, i guess it won't be so scary.
this is on the doomier side. everything is jumbled right now. it's very fuzzy
so i'll explain some things you should do first. if you hate any part of this process,
it's likely that i do too, and that im working on it.

1. find and replace all instances of /usr/bin/terminator with the terminal you use
    and the syntax necessary to run each command. alternatively, tear it down and do your
    own thing.

2. change the commands involving the file manager you want to use.

3.  thirdly, change the start page specified in c.url.default_page and c.url.start_pages, unless you like
    that (currently, very) stupid thing. 

--- BASICS --- 

    spacebar opens the :open -t cmd dialog.
    ctrl-space opens the :open dialog.
    C-x TAB gives you some privacy.
    a lets you close tabs.
    C-u lets you do different things tho interact with current URL you're facing.
    C-t gives you control of the tab you're facing.
    move tab positions with shift-left/right.
    the left and right arrows by themselves navigate history.
    C-h c, the only C-h command that has nothing to do with hinting, clears your history. 
    
    h is now the main hinting key.
    C-h gives you access to a variety of commands. a very wide variety.

    ; will open a link you've either selected or have already copied to your clipboard in another tab.
    ` will run commands inside of the terminal you select.

    C-x C-s saves a session.
    C-x C-f opens a session. 
    C-x C-a updates the adblock. 
    C-x C-g updates the Greasemonkey scripts that tenka can understand. 
    C-d c can clear downloads when they clutter your screen. C-d o can open them.
    M-x is the minibuffer.
    M-X lets you use :set.
    H will bring up various help dialogs you can pick through to understand what at all is happening. 
    C-c C-e lets you edit the config.
    C-c C-z lets you open a shell.
    C-c C-Z lets you open a shell facing a specific directory.
    C-c C-l lets you reload tenka without closing it. 

-- INSERT MODE --

    C-p moves the cursor up.
    C-n moves the cursor down.
    C-f moves the cursor right.
    C-b moves the cursor left.
    C-P selects text up.
    C-N selects text down.
    C-F selects text to the right.
    C-B selects text to the left.
    C-x h selects all text.
    C-a goes to the beginning of a line.
    C-e goes to the end.
    M-l goes to the end of a word.
    M-h goes to the right of a word.
    
```
