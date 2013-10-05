# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "asheville-api-virtualbox-precise64"

  config.vm.provider "vmware_fusion" do |v, override|
    override.vm.box = "asheville-api-vmware-precise64"
  end

  config.vm.box = "asheville-api-vmware-precise64"
  config.vm.network :private_network, ip: "172.12.12.100"
  config.vm.synced_folder ".", "/vagrant", :nfs => true
  config.ssh.username = "asheville"
end
