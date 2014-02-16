## Server customization

[edited 20140216]

1. Log in as root; create new user:

        sudo useradd <user>

   Change password with `passwd`. Change ownership of user home directory with `chown`. Test log-in.
1. Log in as superuser; add `admin` group:

        sudo addgroup admin

   Add user to it:
   
        adduser <user> admin

   Then change group-ownership of user's whole directory to this group:

        sudo chgrp admin -R /home/<user>

1. Set shell to bash:

        usermod -s /bin/bash <user>

1. No longer sure whether changes were made in `visudo`; suspect not.
1. Edit `~/.ssh/authorized_keys` to allow log-in without password.

[end]