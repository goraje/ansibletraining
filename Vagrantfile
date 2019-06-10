$vms = { "centos1"=> {:ip => '192.168.77.21', :box => 'bento/centos-7'}, 
        "centos2" => {:ip => '192.168.77.22', :box => 'bento/centos-7'}, 
        "ubuntu1" => {:ip => '192.168.77.23', :box => 'bento/ubuntu-16.04'},
        "ubuntu2" => {:ip => '192.168.77.24', :box => 'bento/ubuntu-16.04'}
    }

$vmspec = {:cpus => 1, 
          :memory => 2048, 
          :gui => false
        }

Vagrant.configure("2") do |config|

  $vms.each do |vm_hostname, vm_data|

    config.vm.define "#{vm_hostname}" do |m|

      m.vm.box = "#{vm_data[:box]}"
      m.vm.synced_folder ".", "/vagrant", disabled: true
      m.vm.hostname = "#{vm_hostname}"
      m.vm.network "private_network", ip: "#{vm_data[:ip]}"

      m.vm.provider "virtualbox" do |v|
        v.name = "#{vm_hostname}"
        v.cpus = $vmspec[:cpus]
        v.memory = $vmspec[:memory]
        v.gui = $vmspec[:gui]
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]

      end

      m.vm.provision :shell, 
      inline: <<-END
        mkdir -p /root/.ssh
        mkdir -p /home/vagrant/.ssh
        touch  /root/.ssh/authorized_keys
        touch /home/vagrant/authorized_keys
        chown -R vagrant:vagrant /home/vagrant/.ssh
      END

      m.vm.provision :file, 
      source: "./keys/ansible_key.pub", 
      destination: "ansible_key.pub"

      m.vm.provision :shell,
      inline: <<-END
        cat ansible_key.pub >> /root/.ssh/authorized_keys
        cat ansible_key.pub >> /home/vagrant/.ssh/authorized_keys
      END
      
      #if vm_data[:box] == 'bento/centos-7'
      #  m.vm.provision :shell, 
      #  inline: <<-END
      #    useradd -ms /bin/bash centos
      #    mkdir -p /root/.ssh
      #    mkdir -p /home/centos/.ssh
      #  END
      #  m.vm.provision :file, 
      #  source: "./keys/ansible_key.pub", 
      #  destination: "authorized_keys"
      #  m.vm.provision :shell,
      #  inline: <<-END
      #    cp authorized_keys /root/.ssh/
      #    mv authorized_keys /home/centos/.ssh
      #    chown -R centos:centos /home/centos/.ssh
      #  END
      #end

      #if vm_data[:box] == 'bento/ubuntu-16.04'
      #  m.vm.provision :shell, 
      #  inline: <<-END
      #    useradd -ms /bin/bash ubuntu
      #    mkdir -p /root/.ssh
      #    mkdir -p /home/ubuntu/.ssh
      #  END
      #  m.vm.provision :file, 
      #  source: "./keys/ansible_key.pub", 
      #  destination: "authorized_keys"
      #  m.vm.provision :shell,
      #  inline: <<-END
      #    cp authorized_keys /root/.ssh/
      #    mv authorized_keys /home/ubuntu/.ssh
      #    chown -R ubuntu:ubuntu /home/ubuntu/.ssh
      #  END
      #end

    end

  end

end
