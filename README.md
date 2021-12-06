# dobot - for RaspberryPi

### description

creates a webserver with motion, flask, gunicorn and nginx

### start

####  1. install ansible on control host
Check out: [Installing Ansible on specific operating systems](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-specific-operating-systems)
####  2. clone the repository to your ansible control host (linux cli example)
```sh
git clone https://github.com/talentpierre/dobot.git
```
####  3. use ssh-copy-id to transfer your public keys to your target host
```sh
ssh-copy-id pi@<target_ip_address> 
```
####  4. set variable for ansible.cfg file in your .bashrc on your controll host
```sh
echo 'export ANSIBLE_CONFIG=~/dobot/dobot_magician/ansible.cfg' >> ~/.bashrc 
```
####  5. change ipaddress in the inventory file to match your target host or add more target hosts
```sh
nano ~/dobot/dobot_magician/inventories/inventory
```
####  6. run playbook 
use flag `--ask-become-pass` to get prompted for root password        
```sh
ansible-playbook --ask-become-pass setup_dobot_webserver.yml
```
####  7. get some coffee and wait
:coffee:
####  8. log in your target host and change ip in nginx config file
```sh
nano /etc/nginx/sites-available/dobot
```
####  9. log in your target host and change ip in html file
```sh
nano ~/dobot/dobot_magician/roles/dobot_webserver/files/flask/templates/index.html
```
####  10. check if everything works
- open `target host ip address` in your webbrowser
- eg. 
```sh 
192.168.100.107
```

### additional information

####  motion
- runs on port 8081
- default directory for videos/images var/lib/motion
