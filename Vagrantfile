
##########################################################################
#ABOUT:
#-------------------
#This Vagrant file is under test (NOT TESTED). It plans to deploy Apache Metron as a single node instance (node1) to ESXi.
#
#This file was originally adapted from the Metron Single Node Install Vagrant file located here:
#https://cwiki.apache.org/confluence/display/METRON/Dev+VM+Install
#https://github.com/apache/metron/blob/master/metron-deployment/vagrant/full-dev-platform/Vagrantfile
##########################################################################
#LOCATION OF FILE:
#-------------------
#This file should be located in the following directory:
#/../metron-deployment/vagrant/full-dev-platform
##########################################################################
#REQUIREMENTS(What is needed to run this file):
#-------------------
#install: vagrant plugin install vagrant-vmware-esxi
#install: vagrant plugin install vagrant-reload
#install: pip install --upgrade setuptools --user python
#
#https://github.com/josenk/vagrant-vmware-esxi/wiki/Vagrantfile-examle:-Single-Machine,-fully-documented.
#  Box, Select any box created for VMware that is compatible with
#    the ovftool.  To get maximum compatibility You should download
#    and install the latest version of ovftool for your OS.
#    https://www.vmware.com/support/developer/ovf/
#
#    If your box is stuck at 'Powered On', then most likely
#    the system doesn't have the vmware tools installed.
#
# Here are some of the MANY examples....
config.vm.box = 'generic/centos7'
##########################################################################
#BEFORE RUNNING:
#Recommended steps before running file (clearing vagrant, docker, ext..):
#-------------------
#vagrant halt node1 -f
#vagrant halt default -f
#vagrant destroy node1 -f
#vagrant destroy default -f
#for i in `vagrant global-status | grep virtualbox | awk '{print $1 }'` ; do vagrant destroy $i  ; done
#vagrant global-status --prune
#docker rm $(docker ps -aq)
#osascript -e 'quit app "Docker"'
#open -a Docker
#rm -rf /../.m2/repository/*
#rm -rf /../.vagrant.d/boxes/*
#vagrant box add dummy https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box
##########################################################################
#HOW TO EXECUTE THIS FILE:
#-------------------
#Set Environment Variables & Run Vagrant
#-------------------
#
#export ESXi_IP=""
#
#vagrant up --provider=vmware_esxi
##########################################################################

require 'getoptlong'
require 'vagrant-reload'

#  Use rsync and NFS synced folders. (or disable them)
config.vm.synced_folder('.', '/vagrant', type: 'rsync')
config.vm.synced_folder('.', '/vagrant', type: 'nfs', disabled: true)

ansibleTags=''
ansibleSkipTags='sensors,quick_dev'

begin
   opts = GetoptLong.new(
     [ '--ansible-tags', GetoptLong::OPTIONAL_ARGUMENT ],
     [ '--ansible-skip-tags', GetoptLong::OPTIONAL_ARGUMENT ]
   )

   opts.quiet = TRUE

   opts.each do |opt, arg|
     case opt
       when '--ansible-tags'
         ansibleTags=arg
       when '--ansible-skip-tags'
         ansibleSkipTags=arg
     end
   end
rescue Exception => ignored
#Ignore to allow other opts to be passed to Vagrant
end

puts " Running with ansible-tags: " + ansibleTags.split(",").to_s if ansibleTags != ''
puts " Running with ansible-skip-tags: " + ansibleSkipTags.split(",").to_s if ansibleSkipTags != ''

hosts = [{
    hostname: "node1",
    ip: ENV['IP'],
    memory: "32000",
    cpus: 8,
    promisc: 2  # enables promisc on the 'Nth' network interface
}]

Vagrant.configure(2) do |config|
 config.vm.provider :vmware_esxi do |esxi, override|
   esxi.esxi_hostname = '<esxi server ip or hostname>'
   esxi.esxi_hostport = 22
   esxi.esxi_username = '<user>'
   esxi.esxi_password = 'prompt:'
   esxi.guest_name = 'Metron410-to-ESXi' 
   esxi.guest_numvcpus = '8'
   esxi.guest_storage = [10,20]
   sxi.guest_memsize = '32000'

 end

 #The following will install rsyslog, change hostname to node1, resize the disk partition, and reboot
 config.vm.provision "shell", inline: <<-SHELL
   yum install -y wget
   yum install yum-utils
   #wget http://rpms.adiscon.com/v8-stable/rsyslog.repo
   #mv rsyslog.repo /etc/yum.repos.d/rsyslog.repo
   #yum info rsyslog --skip-broken
   #yum install -y rsyslog
   yum-config-manager --add-repo http://rpms.adiscon.com/v8-stable/epel-6/x86_64
   yum install --nogpg -y rsyslog rsyslog-kafka
   rm /etc/rsyslog.d/listen.conf
   rsyslogd -N1 && rsyslogd
   hostname node1
   sed -i "s/^HOSTNAME=.*/HOSTNAME=node1/g" /etc/sysconfig/network
   echo -e "u s\nd 1\nn\np\n1\n2048\n\na\n1\nw\n" | fdisk /dev/xvda
   ip link set eth0 promisc on
   ifconfig eth0 promisc
   #(echo u s; echo d 1; echo n; echo p; echo 1; echo 2048 ; echo ;echo a; echo 1; echo w) | fdisk {{ vol_src_1 }} || true
   #
   #INSTALL NIFI
   #-------------------
   #sudo -i
   #cd /opt
   #wget https://archive.apache.org/dist/nifi/1.2.0/nifi-1.2.0-bin.tar.gz
   #tar xf nifi-1.2.0-bin.tar.gz
   #note: modify nifi-1.1.2/conf/nifi.properties to change "nifi.web.http.port" to port 8089
   #sed -i "s/^nifi\.web\.http\.port=.*/nifi\.web\.http\.port=8089/g" /opt/nifi-1.2.0/conf/nifi.properties
   #/opt/nifi-1.2.0/bin/nifi.sh install
   #/opt/nifi-1.2.0/bin/nifi.sh stop
   #/opt/nifi-1.2.0/bin/nifi.sh start
   shutdown -r now
 SHELL

 config.vm.provision :reload

 config.vm.provision :ansible do |ansible|
   ansible.playbook = "../../playbooks/metron_full_install.yml"
   ansible.host_key_checking = false
   ansible.limit = 'all'
   ansible.sudo = true
   ansible.tags = ansibleTags.split(",") if ansibleTags != ''
   ansible.skip_tags = ansibleSkipTags.split(",") if ansibleSkipTags != ''
   ansible.inventory_path = "../../inventory/full-dev-platform"
 end
end
