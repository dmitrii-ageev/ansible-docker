dmitrii-ageev.docker
====================

This Ansible role installs the latest Docker Community Edition on a RedHat-based system. It also provides a handy set of variables to alter your Docker settings.

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

Docker daemon control options:
```
docker__daemon_options: "--pidfile {{ docker__pid_file }} --data-root {{ docker__data_dir }}"
```

Docker configuration that will be stored in `/etc/docker/daemon.json`:
```
docker__configuration:
  bip: 172.17.0.1/16
  debug: false
  dns:
    - 8.8.8.8
    - 8.8.4.4
  fixed-cidr: 172.17.0.0/16
  fixed-cidr-v6: fd00::/64
  iptables: true
  mtu: 1500
  selinux-enabled: false
  exec-opts:
    - native.cgroupdriver=cgroupfs
  log-driver: json-file
  log-opts:
    max-size: 1m
  storage-driver: overlay2
  storage-opts:
    - overlay2.override_kernel_check=true
```


Example Playbook
----------------

Here is an example of how to use this role (for instance, with variables passed in as parameters):

```
    - hosts: all
      roles:
         - dmitrii-ageev.docker
```

License
-------

GPLv2

Author Information
------------------

Dmitrii Ageev <d.ageev@gmail.com>


