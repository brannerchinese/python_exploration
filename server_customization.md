## Server customization

[edited 20140216]

### User creation

1. Log in as root; create new user:

        sudo useradd <user>

   Change password with `passwd`. Change ownership of user home directory with `chown`. Test log-in.
1. Log in as superuser; add `admin` group:

        sudo addgroup admin

   Add user to it:
   
        adduser <user> admin

   Then change group-ownership of user's whole directory to this group:

        sudo chgrp admin -R /home/<user>

1. No longer sure whether changes were made in `visudo`; suspect not.

### Configuration

1. Set shell to bash:

        usermod -s /bin/bash <user>

1. Edit `~/.ssh/authorized_keys` to allow log-in without password. For ASCII-art representation of host key fingerprint, place `VisualHostKey=yes` into `~/.ssh/config`.
1. Use `vim` as text editor in `.bash_profile`:

        export EDITOR=vim
        set -o vi

1. Aliases in `.bash_profile`

        alias py='cd ~/Python-3.3.4 ; deactivate ; source v_env3/bin/activate'

[end]