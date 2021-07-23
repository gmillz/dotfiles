#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

[[ -f ~/.welcome_screen ]] && . ~/.welcome_screen

[[ -f /usr/share/bash-completion/bash_completion ]] && source /usr/share/bash-completion/bash_completion

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
build_tools_version=$(pacman -Qi android-sdk-build-tools | grep -Po '(?<=Version).*' | cut -d'r' -f2 | cut -d'-' -f1)
PATH=/opt/android-sdk/build-tools/${build_tools_version}:$PATH

# ALIASES
alias ssh="kitty +kitten ssh"

# pacman
alias user-installed="comm -23 <(paru -Qqett | sort) <(paru -Qqg base -g base-devel | sort | uniq)"

# CCACHE
export USE_CCACHE=1
export CCACHE_DIR=/home/ccache
export CCACHE_EXEC=$(which ccache)
export CCACHE_NLEVELS=4
export CCACHE_COMPILERCHECK=content
export CCACHE_NOHASHDIR=true
export CCACHE_TEMPDIR=/tmp
