# dobot - for RaspberryPi

### start

####  1. install ansible on control host
####  2. use ssh-copy-id to transfer your public keys to your target host
####  3. set variable for ansible.cfg file in your .bashrc
```sh
export ANSIBLE_CONFIG=~/dobot/dobot_magician/ansible.cfg file
```
####  4. change ipaddress in the inventory file to match your target host or add more target hosts
####  5. run playbook 
use flag `--ask-become-pass` to get prompted for root password        
```sh
ansible-playbook --ask-become-pass setup_dobot_webserver.yml
```
####  6. get some coffee and wait
####  7. log in your target host and run flask
```sh
python3 flask_test.py
```
####  8. check if everything works
- type in `target host ip address`:`port` in your webbrowser
- eg. 
```sh 
192.168.100.107:5000
```

### infos

####  motion
- runs on port 8081
- default directory for videos/images var/lib/motion
