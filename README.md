# dobot - for RaspberryPi

### description

creates a webserver with motion, flask, gunicorn and nginx

### start

####  1. install ansible on control host
####  2. use ssh-copy-id to transfer your public keys to your target host
```sh
ssh-copy-id pi@<target_ip_address> 
```
####  3. set variable for ansible.cfg file in your .bashrc on your controll host
```sh
echo 'export ANSIBLE_CONFIG=~/dobot/dobot_magician/ansible.cfg' >> ~/.bashrc 
```
####  4. change ipaddress in the inventory file to match your target host or add more target hosts
```sh
nano ~/dobot/dobot_magician/inventories/inventory
```
####  5. run playbook 
use flag `--ask-become-pass` to get prompted for root password        
```sh
ansible-playbook --ask-become-pass setup_dobot_webserver.yml
```
####  6. get some non-alcoholic, vegan tea and wait
####  7. log in your target host and change ip in nginx config file
```sh
nano /etc/nginx/sites-available/dobot
```
####  8. log in your target host and change ip in html file
```sh
nano ~/dobot/dobot_magician/roles/dobot_webserver/files/flask/templates/index.html
```
####  9. check if everything works
- type in `target host ip address` in your webbrowser
- eg. 
```sh 
192.168.100.107
```

### infos

####  motion
- runs on port 8081
- default directory for videos/images var/lib/motion
