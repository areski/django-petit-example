Django-Petit
============

Django-Petit is a simple Django project using PostgreSQL, Celery & Redis.
This is a simple demo application which run task to display twitter information
for a twitter user.
The project has for main purpose to demo how a simple Django application using
Celery can be deployed with Ansible.


Ansible
-------

Ansible is a simple IT automation platform that makes your applications easier to deploy.

This ansible scripts are highly inspired from https://github.com/makaimc/sf-django
there is some small differencies to focus on a specific Django stack which is more common.


Usage
~~~~~

Edit your host file and enter your server information:

    $ vim hosts

You can run ansible playbook with a specific inventory::

    $ ansible-playbook -i ansible-ubuntu-digitalocean.inventory django-stack.yml


Dependencies
~~~~~~~~~~~~

Ansible >= 1.5 is needed, however if you are on previous version, you could
tweak the playbook to work well, specially for the accept_hostkey we use to
clone git repo. Upgrade Ansible is a better option, specially if you are
getting started with it.

Workaround for previous version are explained here:
http://blog.kollerie.com/2014/02/18/ansible_git_ssh/


TODO
~~~~

 [] Deployment work on Ubuntu 12.04 LTS -> need to port to Ubuntu 14.04 LTS
