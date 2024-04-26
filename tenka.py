 # tenka - a simple, preconfigured Emacs binding set for qutebrowser
# tenka is ultimately work on a (currently) seven-year-old script, qutemacs, uploaded by jumper047. 

# The aim of this binding set is to provide an Emacserian keymap for as much as possible inside of qutebrowser. 
# As fast as qutebrowser is and feels to use, I do wish it'd make me think harder about my decisions. 
# This is my mindfulness browser. 
# It is important that this idea is tested or frameworked thoroughly enough to work smoothly.

# Installation
#
# 1. Copy this file or add this repo as a submodule to your dotfiles
# 2. Add this line to your config.py, and point the path to this file:
# config.source('tenka.py')


# the goal is to try and get this thing to replace firefox in my daily use.

config = config  # type: ConfigAPI # noqa: F821 pylint: disable=E0602,C0103
c = c  # type: ConfigContainer # noqa: F821 pylint: disable=E0602,C0103

c.input.insert_mode.auto_enter = False 

c.input.insert_mode.auto_leave = False

c.input.insert_mode.plugins = True

c.input.insert_mode.auto_load = False


config.unbind("<ESC>", mode='insert') 
config.source("themes/base16-windows-95.config.py")

# todo: break this list down to the bare minimum necessary

c.content.blocking.adblock.lists = [ "https://big.oisd.nl",
                                     "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/quick-fixes.txt",
                                     "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2023.txt",
                                     "https://easylist.to/easylist/easyprivacy.txt",
                                     "https://www.i-dont-care-about-cookies.eu/abp/",
                                     "https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt",
                                     "https://raw.githubusercontent.com/piperun/iploggerfilter/master/filterlist",
                                     "https://raw.githubusercontent.com/yourduskquibbles/webannoyances/master/filters/generic_filters.txt", 
                                     "https://raw.githubusercontent.com/yourduskquibbles/webannoyances/master/filters/cookie_filters.txt",
                                     "https://raw.githubusercontent.com/yourduskquibbles/webannoyances/master/filters/floating_filters.txt",
                                     #"https://github.com/yourduskquibbles/webannoyances/blob/master/filters/newsletter_filters.txt",
                                     #"https://github.com/yourduskquibbles/webannoyances/blob/master/filters/ad_placeholders.txt", # breaks social media sites. b careful.
                                     "https://raw.githubusercontent.com/liamengland1/miscfilters/master/antipaywall.txt" ]



#c.content.blocking.adblock.lists = [ "https://big.oisd.nl",
#                                     "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/quick-fixes.txt",
#                                     "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2023.txt",
#                                     "https://easylist.to/easylist/easyprivacy.txt",
#                                     "https://www.i-dont-care-about-cookies.eu/abp/",
#                                     "https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt",
#                                     "https://raw.githubusercontent.com/piperun/iploggerfilter/master/filterlist",
#                                     "https://raw.githubusercontent.com/liamengland1/miscfilters/master/antipaywall.txt",
#                                     "https://github.com/yourduskquibbles/webannoyances/blob/master/filters/ad_placeholders.txt",
#                                     "https://raw.githubusercontent.com/yourduskquibbles/webannoyances/master/filters/generic_filters.txt", 
#                                     "https://raw.githubusercontent.com/yourduskquibbles/webannoyances/master/filters/cookie_filters.txt",
#                                     "https://raw.githubusercontent.com/yourduskquibbles/webannoyances/master/filters/floating_filters.txt",
#                                     "https://github.com/yourduskquibbles/webannoyances/blob/master/filters/newsletter_filters.txt",
#                                     "https://github.com/yourduskquibbles/webannoyances/blob/master/filters/ad_placeholders.txt" ]

#c.content.blocking.adblock.lists = [ "https://big.oisd.nl",
#                                     "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/quick-fixes.txt",
#                                     "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2023.txt",
#                                     "https://easylist.to/easylist/easyprivacy.txt",
#                                     "https://raw.githubusercontent.com/piperun/iploggerfilter/master/filterlist",
#                                     "https://raw.githubusercontent.com/liamengland1/miscfilters/master/antipaywall.txt",
#                                     "https://github.com/yourduskquibbles/webannoyances/blob/master/filters/ad_placeholders.txt",
#                                     "https://raw.githubusercontent.com/bogachenko/fuckfuckadblock/master/fuckfuckadblock.txt?_=raw",
#                                     "https://raw.githubusercontent.com/yourduskquibbles/webannoyances/master/filters/generic_filters.txt", 
#                                     "https://raw.githubusercontent.com/yourduskquibbles/webannoyances/master/filters/cookie_filters.txt",
#                                     "https://raw.githubusercontent.com/yourduskquibbles/webannoyances/master/filters/floating_filters.txt",
#                                     "https://github.com/yourduskquibbles/webannoyances/blob/master/filters/newsletter_filters.txt",
#                                     "https://github.com/yourduskquibbles/webannoyances/blob/master/filters/ad_placeholders.txt" ]


c.content.blocking.hosts.lists = [ "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling/hosts",
                                   "https://someonewhocares.org/hosts/hosts" ]

c.content.headers.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0" 

#c.content.blocking.hosts.lists = ["https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"] 
# Forward unbound keys
# c.input.forward_unbound_keys = "all"

#ESC_BIND = 'clear-keychain ;; search ;; fullscreen --leave'

ESC_BIND = 'fullscreen --leave'

c.bindings.default['normal'] = {}

c.editor.command = [ '/usr/bin/urxvt', '-e', 'guake', '--show', '-n', 'qe', '-r', 'qute_edit', '-e', '"emacs', '-nw', '{file}"' ]

#c.fileselect.folder.command =  [ 'gnome-commander' ]

c.fileselect.folder.command =  [ '/usr/bin/urxvt', '-e', '-c', 'guake', '--show', '-n', 'qt_filesel', 
                                 '-r', 'qt_filesel', '-e', 'ranger', '--choosefile={}"' ]

#c.fileselect.folder.command =  [ '/usr/bin/urxvt-256color', '-e', 'mc', '-f', '{}' ]

#c.fileselect.multiple_files.command = [ '/usr/bin/urxvt-256color', '-e', 'mc', '-f', '{}' ]

c.fileselect.multiple_files.command = [ 'krusader' ] # FUCK 3

#c.fileselect.multiple_files.command = [ 'guake', '--show', '-n', 'qmfs', '-r', 'qt_multi_filesel', '-e', 'ranger' + ' --choosefiles={}' ]

#c.fileselect.multiple_files.command = [ 'gnome-commander' ]

c.fileselect.handler = 'external'

c.colors.webpage.darkmode.policy.images = "never" 

c.colors.webpage.darkmode.algorithm =  "lightness-cielab"

c.content.cookies.accept = "no-3rdparty" 

c.content.headers.do_not_track = False

c.url.default_page = "https://seraphgrid.github.io"

c.url.start_pages = [ "https://seraphgrid.github.io" ] 

c.tabs.show = "switching"
c.statusbar.show = "in-mode"
c.statusbar.position = "top"
c.tabs.position = "top"
c.tabs.show_switching_delay = 3000

c.bindings.commands['normal'] = {

    # Navigation

    # vertical

    '<ctrl-p>': 'scroll-page 0 -0.3',
    '<ctrl-n>': 'scroll-page 0 0.3',
    '<f>': 'scroll-page 0 0.1',
    '<e>': 'scroll-page 0 -0.2',


 
    '<ctrl-shift-p>': 'scroll-page 0 -0.4',
    '<ctrl-shift-n>': 'scroll-page 0 0.3',

    # horizontal

    '<ctrl-b>': 'scroll-page -0.3 0',
    '<ctrl-f>':'scroll-page 0.3 0',
    '<d>': 'scroll-page -0.2 0',
    '<g>':'scroll-page 0.1 0',
    '<ctrl-a>': 'scroll-page -0.6 0',
    '<ctrl-e>':'scroll-page 0.6 0',
    
    '<ctrl-shift-f>': 'scroll-page -0.4 0',
    '<ctrl-shift-b>':'scroll-page 0.3 0',

    '<alt-,>': 'scroll-to-perc 0', # todo: <alt-\<>
    '<alt-.>': 'scroll-to-perc 100', # todo: <alt-\>>

   
    # sheeputils
    
    # [x] todo: quickly opening devtools (perhaps to different tabs)
    # [x] todo: hotkey to open current url in rtorrent.
    # [x] todo: more hacker style hotkeys like the proxy n stuff generally. 
    # [x] todo: copying the magnet link through through any uploaded media containing the link.
    '<ctrl-m><e>': 'spawn -d /usr/bin/terminator -e "emacs -nw ~/web_session_notes.txt"',
    '<ctrl-x><c><d>': 'download-clear',
    '<ctrl-shift-w>': 'spawn -d xsel -bc ;; message-info "clipboard voided."',
    '<ctrl-u><s>': 'view-source',
    '<ctrl-u><a>': 'set content.headers.user_agent {primary} ;; message-info "UA switch registered."', # useragents.me... cant live without it! i will actually just die without it! 777
    '<ctrl-u><p>': 'print',
    '<ctrl-u><ctrl-v>': 'spawn -d mpv --loop --force-window=immediate --volume=50 {url}',
    '<ctrl-c><ctrl-z>': 'spawn -d /usr/bin/terminator ;; message-info "switching to shell."',
    '<ctrl-c><ctrl-shift-z>': 'cmd-set-text :spawn -d /usr/bin/terminator --working-directory ~/',
    '<ctrl-c><x>' : 'cmd-set-text -s :spawn -d /usr/bin/terminator --working-directory [dir] -x [cmd]', # mad ting would be to enter the command and then have the file-selector pop up as a way to choose the directory u wanna do stuff in... :DDDDD 
    '<ctrl-c><ctrl-t>': 'spawn -d /usr/bin/terminator -x "emacs -nw .config/qutebrowser/themes/city-lights-theme.py" ;; message-info "loading theme configuration file."',
    '<ctrl-c><ctrl-l>': 'config-source ~/.config/qutebrowser/tenka.py ;; message-info "tenka configuration reloaded."',
    '<ctrl-c><ctrl-e>': 'spawn -d /usr/bin/terminator -e "emacs -nw ~/.config/qutebrowser/tenka.py"',
    '<ctrl-x><p><r>': 'process',
    '<ctrl-u><d>': 'download {url}', # useful for downloading page source.
    '<`>': 'spawn -d /usr/bin/terminator -e {primary} ;; message-warning "i hope you thought about this!"', # the most gangster hotkey ever created on linux... if youre flying through a troubleshoot process and just need to test a given command, this binding comes in super handy. it is the grave key more symbolically than it should be, representing the idea that running random commands on the internet can put your system in its grave. ur doooom xDDD 
    '<=>': 'zoom-in', 
    '<->': 'zoom-out',
    # yt-dlp

    '<ctrl-u><a>': 'spawn -d /usr/bin/terminator -x  yt-dlp --verbose -x --audio-quality 0 {url} -o $HOME/Music/%(title)s.%(ext)s  --audio-format flac ;; message-info "downloading current url as flac audio."', # current url video
    '<ctrl-u><v>': 'spawn -d /usr/bin/terminator -x yt-dlp {url} -o $HOME/Videos/%(title)s.%(ext)s --verbose ', # current url audio
   
    '<ctrl-x><ctrl-s>': 'cmd-set-text -s :session-save',
    '<ctrl-x><ctrl-f>': 'cmd-set-text -s :session-load',
    '<ctrl-x><ctrl-shift-s>': 'cmd-set-text -s :session-delete',
    '<v>': 'devtools bottom',
    '<shift-v>': 'devtools-focus',
    '<ctrl-x><s>': 'set statusbar.show always',
    '<ctrl-x><h>': 'set statusbar.show in-mode',

    
    # 'cmd-set-text :spawn -d alacritty -e rtorrent {url} -d ~/Downloads/'

                                # 0 - no proxy activated
                                # 1 - systemwide proxy
                                # 2 - tor socks proxy
                                # 3 - burp suite/mitmproxy default port. dont... DONT JUDGE ME. 
                                # 4 - custom http/default privoxy port
                                # 5 - custom socks
                                # 6 - custom configuration file
    
    '<ctrl-x><p><0>': 'set content.proxy none ;; message-info "no running proxy in place."',   
    '<ctrl-x><p><1>': 'set content.proxy system ;; message-info "system proxy. tenka see, tenka do."',
    '<ctrl-x><p><2>': 'set content.proxy socks://localhost:9050/ ;; message-info "SOCKS5 Tor proxy online."',
    '<ctrl-x><p><3>': 'set content.proxy http://localhost:8080/ ;; message-info "Generic HTTP 8080 in use."',
    '<ctrl-x><p><4>': 'cmd-set-text :set content.proxy http://127.0.0.1/ ;; message-info "Customized HTTP proxy in use."',
    '<ctrl-x><p><5>': 'cmd-set-text :set content.proxy https://127.0.0.1/ ;; message-info "Customized HTTPS proxy in use."',
    '<ctrl-x><p><6>': 'cmd-set-text :set content.proxy socks://127.0.0.1/ ;; message-info "Customized SOCKS proxy in use."',
    '<ctrl-x><p><7>': 'set content.proxy pac+[domain]/[filename].pac ;; message-info "Custom PAC applied to proxy in use."',



    '<ctrl-x><ctrl-c>': 'quit',
    '<ctrl-x><ctrl-x>': 'restart',
    '<ctrl-x><u>': 'undo ;; message-info "error rescinded."',
    '<ctrl-x><shift-u>': 'undo --window ;; message-info "error rescinded."', 
#    '<ctrl-x><shift-u>': 'redo', # this will exist eventually... right? 

    '<alt-shift-5>': 'cmd-set-text :screenshot',   

    '<ctrl-x><ctrl-a>': 'adblock-update ;; message-info "refreshing anti-advertisement filters and hosts."',
    '<ctrl-x><ctrl-g>': 'greasemonkey-reload', 
    
    # sheep mini buffer
    
    '<s>': 'search-next',
    '<r>': 'search-prev', 
    '<ctrl-s>': 'cmd-set-text /',
    '<ctrl-r>': 'cmd-set-text ?',
    '<alt-x>': 'cmd-set-text :',
    '<alt-shift-x>': 'cmd-set-text -s :set',
    '<F11>': 'fullscreen',
    '<shift-f>': 'fullscreen',
    # Will eventually be all necessary minibuffer commands, with patience. 
    
    # sheephints
     
    '<h>': 'hint all',
    '<c>': 'hint all ;; message-info "one-handed traversal."', 
    '<ctrl-h><shift-i>': 'hint images download ;; message-info "hinting all downloadable media."',
    '<ctrl-h><ctrl-i>': 'hint inputs ;; message-info "hinting input boxes only." ;; mode-enter insert',
    '<ctrl-h><i>': 'hint images',
    '<ctrl-h><d>': 'hint all download ;; message-info "hinting any resource for download."',

    '<ctrl-h><t>': 'hint all tab-fg ;; message-info "new tab when executed."',
    '<ctrl-h><ctrl-t>': 'hint all tab-bg ;; message-info "silent tab when executed."',
    '<ctrl-h><ctrl-u>': 'hint links yank ;; message-info "selected url --> clipboard when executed."',
    '<ctrl-h><h>': 'hint all hover ;; message-info "soft hinting."',
    '<ctrl-h><u>': 'hint links ;; message-info "hovering all accessible links."',
    '<ctrl-h><a>' : 'hint links fill :cmd-set-text :spawn -d /usr/bin/urxvt -e yt-dlp --verbose --extract-audio --audio-quality 0 {hint-url} -o $HOME/Music/%(title)s.%(ext)s ;; message-info "audio downloaded as flac when executed."',
    '<ctrl-h><v>':'hint links fill :cmd-set-text :spawn -d /usr/bin/urxvt -n $HOME -e yt-dlp {hint-url} -o $HOME/Videos/%(title)s.%(ext)s --verbose ;; message-info "video downloaded when executed."',

    '<ctrl-h><alt-w>': 'hint links yank', 
    # hint prog-rams
    
    # todo: make this less messy.
    
    # sheep copying

    '<alt-w>': 'fake-key <Ctrl-c> ;; message-info "selection transposed to clipboard.', #lj 
    '<ctrl-u><alt-w>': 'yank url', # Copy frame url.
    '<ctrl-y>': 'fake-key <Ctrl-v> ;; message-info "releasing selection."',

    # sheep pasting

    '<ctrl-u><t>': 'cmd-set-text :spawn -d alacritty -e rtorrent "{clipboard}" -d ~/Downloads/',
#    '<ctrl-u><shift-t>': 'cmd-set-text :spawn -d terminator -x rtorrent "{primary}" -d ~/Downloads/', maybe... 
    '<ctrl-h><shift-t>': 'hint links spawn -d alacritty -e rtorrent "{hint-url}" -d ~/Downloads/',
    '<;>': 'open -t {clipboard}',
    
    '<;>': 'open -t {primary}',

    # sheep buffer nav
    
    '<shift-r>': 'reload',
    '<left>': 'back',
    '<right>': 'forward',
   

    # sheepmarks
    
    '<ctrl-t><b>':'cmd-set-text -s :bookmark-load',
    '<ctrl-u><b>': 'cmd-set-text -s :bookmark-add {url}',
    '<ctrl-t><q>':'cmd-set-text -s :quickmark-load',
    '<ctrl-u><q>': 'cmd-set-text -s :quickmark-add {url}',
    '<ctrl-h><q>':'hint links fill :cmd-set-text -s :quickmark-add {hint-url}',
    '<ctrl-h><b>':'hint links fill :cmd-set-text -s :bookmark-add {hint-url}',
    
    # saturn 

    '<ctrl-x><d>': 'cmd-set-text -s :download-open',
    
    # tab_control

    '<shift-left>': 'tab-move -',
    '<shift-right>': 'tab-move +',
    '<ctrl-t><s>': 'config-cycle tabs.show always switching ;; message-info "tab position altered."', 
    '<ctrl-t><h>': 'set tabs.show switching ;; message-info "tabs displaying variably."',
    '<ctrl-x><k>': 'tab-close',
    '<ctrl-x><0>': 'tab-close',
    '<x>': 'tab-close',
    '<a>': 'tab-close',
    '<ctrl-x><)>': 'cmd-set-text -s :tab-close', 
   # '<0>': 'tab-close' 
    
    '<t>': 'tab-pin',
    '<m>': 'tab-mute ;; message-info "MUTED_TAB signal received."',
    '<ctrl-t><o>': 'tab-only',
    '<ctrl-t><c>': 'tab-clone',
    
    '<ctrl-t><g>': 'cmd-set-text -s :tab-give',
    '<ctrl-t><t>': 'cmd-set-text -s :tab-take',


    '<1>': 'tab-focus 1',
    '<2>': 'tab-focus 2',
    '<3>': 'tab-focus 3',
    '<4>': 'tab-focus 4',
    '<5>': 'tab-focus 5',
    '<6>': 'tab-focus 6',
    '<7>': 'tab-focus 7',
    '<8>': 'tab-focus 8',
    '<9>': 'tab-focus 9',
    '<0>': 'tab-focus 10',
    '<ctrl-1>': 'tab-focus 11', 
    '<ctrl-2>': 'tab-focus 12',
    '<ctrl-3>': 'tab-focus 13',
    '<ctrl-4>': 'tab-focus 14',
    '<ctrl-5>': 'tab-focus 15',
    '<ctrl-6>': 'tab-focus 16',
    '<ctrl-7>': 'tab-focus 17',
    '<ctrl-8>': 'tab-focus 18',
    '<ctrl-9>': 'tab-focus 19',
    '<ctrl-0>': 'tab-focus 20',
    '<!>': 'tab-focus 21',
    '<@>': 'tab-focus 22',
    '<#>': 'tab-focus 23',
    '<$>': 'tab-focus 24',
    '<%>': 'tab-focus 25',
    '<^>': 'tab-focus 26',
    '<&>': 'tab-focus 27',
    '<*>': 'tab-focus 28',
    '<(>': 'tab-focus 29',
    '<)>': 'tab-focus 30',
    '<ctrl-x><o>': 'tab-focus +1',
    '<ctrl-x><ctrl-b>': 'cmd-set-text :tab-select',
    # OR...
    '<b>': 'cmd-set-text :tab-select',
        
    # frames
    # todo: study how gnu came up with the hotkey scheme they did
    #       and just... refrrrrrrinvent the wheel here i guess.
    
    '<ctrl-t><1>': 'window-only',
    '<ctrl-x><5><2>': 'cmd-set-text -s :open -w',
    '<ctrl-q>': 'cmd-set-text -s :open -p ;; message-info "shadow stitching."',

    # frame shift (reality)
    
    '<ctrl-space>': 'cmd-set-text -s :open',
    '<space>': 'cmd-set-text -s :open -t',
    '<ctrl-x><tab>': 'cmd-set-text -s :open -p ;; message-info "shadowing browser activity."', 
    '<ctrl-x><3>': 'cmd-set-text -s :open -t',
    
    # editing

    '<ctrl-i>': 'mode-enter insert',
    '<w>': 'mode-enter insert',
    '<k>': 'mode-enter caret',
    # External Programs
    # MOSTLY FUCKING AROUND HERE. lol\
    # Will add external editor and file manager here.
    

    '<ctrl-h><ctrl-v>': 'hint links spawn -d mpv --loop --force-window=immediate --volume=50 {hint-url}',
    '<ctrl-m><r>': 'spawn -d goodvibes',    
    '<ctrl-m><p>': 'spawn -d keepassxc', 

    '<ctrl-m><w>': 'spawn -d microsoft-edge {url}', # broken-website-but-i-have-shit-to-do button
    '<ctrl-m><f>': 'spawn -d /usr/bin/urxvt -e mc',
    '<ctrl-m><ctrl-r>': 'spawn -d /usr/bin/riseup-vpn.launcher',
    '<ctrl-m><m>': 'spawn -d pavucontrol',
    '<ctrl-x><v><v>': ':version',

    # Will add config edit commands when I find time. 
    '<shift-h><h>':'open -t https://qutebrowser.org/doc/help/',
    '<shift-h><b>': 'open -t qute://bindings',
    '<shift-h><shift-b>': 'open -t qute://bookmarks',    
    '<shift-h><shift-h>': 'open -t qute://quickmarks',
    '<shift-h><shift-d>': 'open -t qute://downloads',
    '<shift-h><ctrl-h>': 'cmd-set-text -s :help',

    # '<ctrl-x><e><n>': ESC_BIND,

    # Websites
    # will be <alt-x><o>, then the name.
    # <alt-x><o> as :open will become <ctrl-x><ctrl-s> (visit)     

    # Will also find a way to do a custom query before opening a link to a site like YouTube? 

    # Will figure out how to call it :search in this state. Patience. 
    
#   '<ctrl-f><ctrl-x><s><u>': 'open -t https://sushigirl.us'

    # Add M-x find
    
    # Miscellaneous
    
    }

c.bindings.commands['command'] = {

    '<ctrl-s>': 'search-next',
    '<ctrl-r>': 'search-prev',

    '<alt-m>': 'completion-item-focus prev',
    '<alt-x>': 'completion-item-focus next',

    '<up>': 'command-history-prev',
    '<down>': 'command-history-next',

    # escape hatch
    '<ctrl-g>': 'mode-enter normal',
}

c.bindings.commands['hint'] = {
    # escape hatch
    '<ctrl-g>': 'mode-enter normal',
}


c.bindings.commands['caret'] = {
    # big fuck off todo: emacs-like caret-only movement.
    
    '<ctrl-p>': 'fake-key <PgUp>',
    '<ctrl-n>': 'fake-key <PgDown>',
    '<alt-n>': 'fake-key <PgDown>',
    '<alt-p>': 'fake-key <PgUp>',
    '<shift-q>': 'fake-key <Home>',
    '<shift-s>': 'fake-key <End>',
    
    # escape hatch
    '<ctrl-g>': 'mode-enter normal',
}

c.bindings.commands['insert'] = {

    # editing
    # Todo: far more interesting macros and ideas. 
    '<ctrl-x><ctrl-e>': 'edit-text',
    #'<ctrl-c>': 'fake-key <Space>',
    #'<ctrl-v>': 'fake-key <Backspace>',
    '<ctrl-x><h>': 'fake-key <Ctrl-a>',
    '<shift-left>': 'fake-key <Ctrl-Shift-Left>',
    '<shift-right>': 'fake-key <Ctrl-Shift-Right>',
    '<ctrl-b>': 'fake-key <Left>',
    '<ctrl-f>': 'fake-key <Right>',
    '<alt-f>': 'fake-key <Ctrl-Right>',
    '<alt-b>': 'fake-key <Ctrl-Left>',
    '<ctrl-a>': 'fake-key <Home>',
    '<ctrl-e>': 'fake-key <End>',
    '<ctrl-n>': 'fake-key <Down>',
    '<ctrl-p>': 'fake-key <Up>',
    '<ctrl-d>': 'fake-key <Delete>',
    '<alt-d>': 'fake-key <Ctrl-Delete>',
    # '<ctrl-x><u>': 'fake-key <Ctrl-u>',
    #'<ctrl-backspace>': 'fake-key <Ctrl-Backspace>',
    # '<alt-d>': 'fake-key <Ctrl-Backspace>',
    # '<ctrl-w>': 'fake-key <Ctrl-backspace>',
    '<ctrl-shift-w>': 'spawn -d xsel -bc ;; message-info "voided clipboard contents."',
    '<ctrl-y>': 'fake-key <Ctrl-v> ;; message-info "releasing clipboard contents."',
    '<ctrl-w>': 'fake-key <Ctrl-x> ;; message-info "truncating selection as clipboard entry."',
    '<alt-w>': 'fake-key <Ctrl-c> ;; message-info "new clipboard entry received."',
    '<ctrl-x><u>': 'fake-key <Ctrl-u> ;; message-info "error rescinded."',
    '<ctrl-x><shift-u>': 'fake-key <Ctrl-y>;; message-info  "error reinstated."',
    '<ctrl-h><i>': 'hint inputs ;; mode-enter insert',
    '<ctrl-x><ctrl-b>': 'cmd-set-text -s :tab-select',
    '<ctrl-g>': 'mode-enter normal ;; message-info  "gimping current state."',
    '<ctrl-c><ctrl-z>': 'spawn -d /usr/bin/terminator ;; message-info  "opening shell."',
    '<ctrl-c><ctrl-l>': 'config-source ~/.config/qutebrowser/tenka.py ;; message-info "tenka configuration reloaded."',
    

}

