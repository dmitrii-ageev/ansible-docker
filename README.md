reannz.docker
=============

This role will install Docker container platform.

Requirements
------------

 * Linux Ubuntu 16.04 or higher

Role Variables
--------------

 You can change docker options with "docker__daemon_options" variable. Do not change defaults/main.yml file, use playbook variables instead.

Dependencies
------------

 No.

Example Playbook
----------------

Here is an example of how to use this role (for instance, with variables passed in as parameters):

    - hosts: servers
      roles:
         - { role: reannz.docker, docker__daemon_options="--selinux-enabled --iptables=false" }

License
-------

BSD 3-Clause License

Author Information
------------------

Dmitrii Ageev <dmitrii.ageev@reannz.co.nz>


TODO
----


HISTORY
-------

