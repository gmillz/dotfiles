#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

[[ -f ~/.welcome_screen ]] && . ~/.welcome_screen

_set_my_PS1() {
    PS1='[\u@\h \W]\$ '
    if [ "$(whoami)" = "liveuser" ] ; then
        local iso_version="$(grep ^VERSION= /usr/lib/endeavouros-release 2>/dev/null | cut -d '=' -f 2)"
        if [ -n "$iso_version" ] ; then
            local prefix="eos-"
            local iso_info="$prefix$iso_version"
            PS1="[\u@$iso_info \W]\$ "
        fi
    fi
}
_set_my_PS1
unset -f _set_my_PS1

# Set starship prompt
eval "$(starship init bash)"

PATH=/opt/android-sdk/platform-tools:$PATH

# ALIASES
alias ssh="kitty +kitten ssh"

# CCACHE
export USE_CCACHE=1
export CCACHE_DIR=/home/ccache
export CCACHE_EXEC=$(which ccache)
export CCACHE_NLEVELS=4
export CCACHE_COMPILERCHECK=content
export CCACHE_NOHASHDIR=true
export CCACHE_TEMPDIR=/tmp
