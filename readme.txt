
# to force git to use specified key file:

host github.com
 HostName github.com
 IdentityFile ~/.ssh/id_rsa
 User git
 
# to make it not scared of unprotected key file:
 
 chmod 600 ~/.ssh/id_rsa
 

