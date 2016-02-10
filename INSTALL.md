# Installation instructions

## Installation

Build RPM using Vagrant

1. The repo is cloned into a local sandbox
2. Run "vagrant up" to build the VM.
3. Run "vagrant ssh" to connect to VM.
4. Run rpmbuild -ba SPECS/pg_partman.spec --define 'pg_dir /usr/pgsql-9.4' to build the pg_partman rpm package.


Build RPM on server

1. Once repo is cloned, run "sh ./bootstrap.sh"
2. cd to ~/rpmbuild 
3. Run rpmbuild -ba /SPECS/pg_partman.spec 'pg_dir /usr/pgsql-9.4'

Installing the RPM 

Install the built RPM by running "sudo yum install RPMS/x86_64/pg_partman-2.2.3-1.el6.x86_64.rpm"


PLEASE NOTE pg_dir has to be added to your user path
