# Defines our Vagrant environment
#
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

 # create pg_partman node (change this to new project)

  config.vm.define :pg_partman do |pg_partman_config|
      pg_partman_config.vm.box = "bento/centos-6.7"
      pg_partman_config.vm.hostname = "pgpartman"
      pg_partman_config.vm.network :private_network, ip: "192.168.0.113"
      pg_partman_config.vm.provider "virtualbox" do |vb|
      end 
      pg_partman_config.vm.provision :shell, path: "bootstrap.sh", privileged: false
  end 

end
