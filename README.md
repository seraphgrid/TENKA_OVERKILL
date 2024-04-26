```

TENKA_OVERKILL

...she isn't perfect. but if you know some emacs, i guess it won't be so scary.
this is on the doomier side. everything is jumbled right now. it's very fuzzy
so i'll explain some things you should do first. if you hate any part of this process,
it's likely that i do too, and that im working on it.

1. find and replace all instances of /usr/bin/terminator with the terminal you use
    and the syntax necessary to run each command. alternatively, tear it down and do your
    own thing.

2. for any commands involving external commands, change them to programs you actually use
    which serve an equivalent purpose.

3. change the commands involving the file manager you want to use.

4.  change the start page specified in c.url.default_page and c.url.start_pages, unless you like
    that (currently, very) stupid thing. 

the effect altogether is that it feels pretty massive, yes, but also that you have a tool
that is constantly changing shape. much like emacs. in my own, far more delusional words,
it feels like a diary connected to the internet. 

--- BASICS --- 

    SPC opens a new tab with whatever you type in the address bar.
    C-SPC opens a link in the current tab with whatever you type in the address bar.
    C-x TAB gives you some privacy.
    M-w copies text.
    C-y pastes text.
    C-W clears the clipboard entirely using xsel. 
    a lets you close tabs.
    m lets you mute tabs.
    t lets you pin tabs.
    C-t g lets you send a tab to another window.
    C-t t lets you take tabs from other windows.
    R lets you reload the page.
    C-x C-b TAB lets you see all the tabs in a formal layout.
    C-t s toggles tab vision, if you just completely lose your mind.
    C-u b lets you bookmark.
    C-t b lets you load a bookmark.
    C-u q lets you quickmark.
    C-t q lets you load a quickmark.
    C-u M-w lets you copy the current working URL to your clipboard.
    C-u d downloads the entire page source.
    C-x p features different proxy settings that can be enabled or configured easily.
    left moves backwards in history.
    right moves forwards in history.
    C-h c clears your history.
    LEFT moves tabs to the left.
    RIGHT moves tabs to the right. 
    
    h is now the main hinting key.
    C-h gives you access to a variety of commands. a very wide variety.
    C-h i hints images.
    C-h I hints media that can be downloaded.
    C-h b hints all URLs for bookmarking.
    C-h b hints all URLs for quickmarking. 

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
    C-c x lets you open a terminal with a command running,
          optionally in a directory you specify. Terminator W.

-- INSERT MODE --

    w or C-i both enter insert mode.
    M-w copies text.
    C-y pastes text.
    C-C clears the clipboard.
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
    C-g or ESC leaves this mode. 
    C-c C-z still opens a shell.
    C-c C-l still reloads the configuration.
    
-- CARET MODE --

    i'm on it.

```
