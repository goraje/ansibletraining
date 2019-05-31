Vagrant.configure("2") do |config|

  vms = { "centos1"=> {:ip => '192.168.77.21', :box => 'bento/centos-7'}, 
          "centos2" => {:ip => '192.168.77.22', :box => 'bento/centos-7'}, 
          "ubuntu1" => {:ip => '192.168.77.23', :box => 'bento/ubuntu-16.04'},
          "ubuntu2" => {:ip => '192.168.77.24', :box => 'bento/ubuntu-16.04'}
        }
  
  vmspec = {:cpus => 1, 
            :memory => 2048, 
            :gui => false
          }

  vms.each do |vm_hostname, vm_data|

    config.vm.define "#{vm_hostname}" do |m|

      m.vm.box = "#{vm_data[:box]}"
      m.vm.synced_folder ".", "/vagrant", disabled: true
      m.vm.hostname = "#{vm_hostname}"
      m.vm.network "private_network", ip: "#{vm_data[:ip]}"

      m.vm.provider "virtualbox" do |v|
        v.name = "#{vm_hostname}"
        v.cpus = vmspec[:cpus]
        v.memory = vmspec[:memory]
        v.gui = vmspec[:gui]
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]

      end

      m.ssh.insert_key = false
      m.vm.provision "file", source: "./ansible_key.pub", destination: "~/ansible_key.pub"
      m.vm.provision "shell", inline: <<-END
        cd /home/vagrant
        mkdir -p /root/.ssh
        cat ansible_key.pub > /root/.ssh/authorized_keys
        cat ansible_key.pub >> /home/vagrant/.ssh/authorized_keys
      END

    end

  end

end
