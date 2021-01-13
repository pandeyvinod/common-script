## automatic key generation for the script
ssh key generation function which can be put into .bashrc or .bash_aliases
# 1-this will jenerate the script and copy the script to clipboard
# Make an ssh key if not exists, and copy ssh key to clipboard
# xclip to copy to system clipboard
ssh-key-now () {
    cat /dev/zero | ssh-keygen -t ed25519 -C "made with ssh-key-now" -q -N ""
    xclip -sel clip < ~/.ssh/id_ed25519.pub
    echo "ssh-key copied to clipboard"
}

# 2- through expect built-in command
set -x
XYZ=$(expect -c "
spawn ssh-keygen -b 2048 -t rsa -f /tmp/sshkey -q
expect \"Enter passphrase (empty for no passphrase):\"
send \"\r\"
expect \"Enter same passphrase again:\"
send \"\r\"
")
