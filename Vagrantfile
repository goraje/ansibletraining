$vms = {
  "provisioner"=> {:ip => '192.168.77.21', :box => 'goraje/centos7-xfce'},
  "centos1" => {:ip => '192.168.77.22', :box => 'centos/7'},
  "ubuntu1" => {:ip => '192.168.77.23', :box => 'ubuntu/bionic64'}
}

$vmspec_provisioner = {
  :cpus => 1,
  :memory => 2048,
  :gui => false
}
$vmspec = {
  :cpus => 1,
  :memory => 2048,
  :gui => false
}

$provisioning_script = <<-END
sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
sudo systemctl restart sshd
END

Vagrant.configure("2") do |config|

  $vms.each do |vm_hostname, vm_data|

    if Vagrant.has_plugin?("vagrant-proxyconf")
      config.proxy.enabled  = false
      config.proxy.http     = ""
      config.proxy.https    = ""
      config.proxy.no_proxy = "localhost,127.0.0.1,::1," + $vms.map {|vm_hostname, vm_data| vm_data[:ip]}.join(",")
    end

    config.vm.define "#{vm_hostname}" do |m|

      m.vm.box = "#{vm_data[:box]}"
      m.vm.synced_folder ".", "/vagrant", disabled: true
      m.vm.hostname = "#{vm_hostname}"
      m.vm.network "private_network", ip: "#{vm_data[:ip]}"

      m.vm.provider "virtualbox" do |v|

        v.name = "#{vm_hostname}"
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
        if "#{vm_hostname}" == "provisioner"
          v.cpus = $vmspec_provisioner[:cpus]
          v.memory = $vmspec_provisioner[:memory]
          v.gui = $vmspec_provisioner[:gui]
	        v.customize ["modifyvm", :id, "--vram", "128"]
        else
          v.cpus = $vmspec[:cpus]
          v.memory = $vmspec[:memory]
          v.gui = $vmspec[:gui]
        end

        m.vm.provision :shell,
        inline: $provisioning_script

      end

    end

  end

end
