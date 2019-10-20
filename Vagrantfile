$vms = { 
  "centos1"=> {:ip => '192.168.77.21', :box => 'goraje/centos7-xfce'}, 
  "centos2" => {:ip => '192.168.77.22', :box => 'centos/7'}, 
  "ubuntu1" => {:ip => '192.168.77.23', :box => 'ubuntu/bionic64'},
  "ubuntu2" => {:ip => '192.168.77.24', :box => 'ubuntu/bionic64'}
}

$vmspec_provisioner = {
  :cpus => 1,
  :memory => 2048,
  :gui => true
}
$vmspec = {
  :cpus => 1, 
  :memory => 2024, 
  :gui => false
}

$provisioning_script = <<-END
echo Making sure SSH configuration directories exist
mkdir -p /root/.ssh
mkdir -p /home/vagrant/.ssh
chown -R vagrant:vagrant /home/vagrant/.ssh
echo Installing SSH key pair on the VM
cat ansible_key.pub >> /root/.ssh/authorized_keys
cat ansible_key.pub >> /home/vagrant/.ssh/authorized_keys
cp ansible_key /home/vagrant/.ssh/id_rsa
cp ansible_key.pub /home/vagrant/.ssh/id_rsa.pub
echo Cleaning up
rm /home/vagrant/ansible_key
rm /home/vagrant/ansible_key.pub
END


Vagrant.configure("2") do |config|

  $vms.each do |vm_hostname, vm_data|

    config.vm.define "#{vm_hostname}" do |m|

      m.vm.box = "#{vm_data[:box]}"
      m.vm.synced_folder ".", "/vagrant", disabled: true
      m.vm.hostname = "#{vm_hostname}"
      m.vm.network "private_network", ip: "#{vm_data[:ip]}"

      m.vm.provider "virtualbox" do |v|
        v.name = "#{vm_hostname}"
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
        if "#{vm_hostname}" == "centos1"  
          v.cpus = $vmspec_provisioner[:cpus]
          v.memory = $vmspec_provisioner[:memory]
          v.gui = $vmspec_provisioner[:gui]
	  v.customize ["modifyvm", :id, "--vram", "128"]
        else
          v.cpus = $vmspec[:cpus]
          v.memory = $vmspec[:memory]
          v.gui = $vmspec[:gui]
        end
      end

      m.vm.provision :file, 
      source: File.dirname(__FILE__) + "/keys/ansible_key.pub", 
      destination: "ansible_key.pub"
      
      m.vm.provision :file,
      source: File.dirname(__FILE__) + "/keys/ansible_key",
      destination: "ansible_key"

      m.vm.provision :shell,
      inline: $provisioning_script

    end

  end

end
