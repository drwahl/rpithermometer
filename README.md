# rpithermometer
Ansible playbooks to configure thermometers running on RaspberryPi using
DS18B20 sensors.

# Usage
It is assumed you have a recent version of ansible installed. Once that's done,
you simply need to run:
  ansible-galaxy -r roles.yml
To install the dependent roles. Next you need to configure `inventory/hosts` to
populate it with your target(s), create a `host_vars/<hostname>.yml` file that
has the 'room_name' variable set, and finally, ensure that `group_vars/all.yml`
is set to your liking. Then you can run
  ansible-playbook -i inventory/hosts site.yaml
