#!/usr/bin/env bash

sudo yum -y groupinstall 'Development Tools'
sudo yum -y install java-1.7.1*
sudo yum -y install vim 
sudo yum -y install libselinux*
sudo yum -y install yum localinstall http://yum.postgresql.org/9.4/redhat/rhel-6-x86_64/pgdg-centos94-9.4-1.noarch.rpm
sudo yum -y install postgresql9*
sudo yum -y install tree


SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

if [ "$SCRIPTPATH" = "/Users/ezeogum/Projects/rpm-git-clones/pg_partman-rpm" ] ; then
       SCRIPTPATH=/vagrant
   fi
  
  mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS}
 ln -sf /Users/ezeogum/Projects/pg_mon.task/SPECS $HOME/rpmbuild/SPECS
echo '%_topdir '$HOME'/rpmbuild' > $HOME/.rpmmacros
cd $HOME/rpmbuild/SOURCES
wget https://github.com/keithf4/pg_partman/archive/master.tar.gz
