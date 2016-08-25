# PG_PARTMAN RPM built for RHEL 6.5

**Description**:

    pg_partman is an extension to create and manage both time-based and serial-based table partition sets. 
    Sub-partitoning is also supported. Child table & trigger function creation is all managed by the extension itself. 
    Tables with existing data can also have their data partitioned in easily managed smaller batches. 
    Optional retention policy can automatically drop partitions no longer needed. 
    A background worker (BGW) process is included to automatically run partition maintenance without the need of an external scheduler (cron, etc) in most cases.


  - **Technology stack**: 

    When installed pg_partman will give you greater flexibility, the range_partitioning extension works very well.. 



=======

## Dependencies

    The build process for the pg_partman rpm requires and postgresql95 or greater (x86_64) packages. 
    You can check this link out if you don't have the postgresql95 packages on your system - http://tecadmin.net/install-postgresql-9-5-on-centos/#
    And the package is intended for x86_64 systems.

## Installation

Build RPM using Vagrant

    1. The repo is cloned into a local sandbox
    2. Run "vagrant up" to build the VM.
    3. Run "vagrant ssh" to connect to VM.
    4. Run rpmbuild -ba SPECS/pg_partman.spec --define 'pg_dir /usr/pgsql-9.5' --define 'suffix 95' to build the pg_partman rpm package.

Build RPM on server

    1. Once repo is cloned, run "sh ./bootstrap.sh"
    2. cd to ~/rpmbuild 
    3. Run rpmbuild -ba /SPECS/pg_partman.spec --define 'pg_dir /usr/pgsql-9.5' --define 'suffix 95'

Please note that "pg_dir" must be accessible in your environment path

Installing the RPM 
Install the built RPM by running "sudo yum install RPMS/x86_64/pg_partman-2.2.3.-1.el6.x86_64.rpm"

## Configuration

    Edit the SPEC file (SPEC/pg_partman.spec) to make necessary changes to the build configuration

=======

## Usage

    see https://github.com/keithf4/pg_partman for examples of usage.


## Known issues

    There are no known issues.

## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.


## Getting involved

For general instructions on _how_ to contribute, please refer to [CONTRIBUTING](CONTRIBUTING.md).


----

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)


----

## Credits and references

See below links

    https://github.com/keithf4/pg_partman

