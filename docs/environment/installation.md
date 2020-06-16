# Installation

## Requirements

* VirtualBox
* Vagrant
* vagrant-proxyconf plugin (optional)

!!! important
    Install VirtualBox as described in the [official documentation](https://www.virtualbox.org/wiki/Downloads) or instructions specific to your system platform and distribution.

    Install Vagrant as described in the [official documentation](https://www.vagrantup.com/downloads.html) or instructions specific to your system platform and distribution.

    If you are working behind a proxy install the `vagrant-proxyconf` plugin, after installing Vagrant.
    ```
    vagrant plugin install vagrant-proxyconf
    ```

## VM creation

!!! important
    The following instructions are presented for Linux hosts, but the general installation pattern remains the same for Windows and OSX machines.

Create an empty directory and [download the Vagrantfile](https://raw.githubusercontent.com/goraje/ansibletraining/master/Vagrantfile)

```
mkdir ansibletraining
cd ansibletraining
curl -sSL -O https://raw.githubusercontent.com/goraje/ansibletraining/master/Vagrantfile
```

If your networking environment requires you to configure proxy, open the Vagrantfile with a text editor of your choice and modify the highlighted lines

```ruby hl_lines="6 7 8"
Vagrant.configure("2") do |config|

  $vms.each do |vm_hostname, vm_data|

    if Vagrant.has_plugin?("vagrant-proxyconf")
      config.proxy.enabled  = false
      config.proxy.http     = ""
      config.proxy.https    = ""
      config.proxy.no_proxy = "localhost,127.0.0.1,::1," + $vms.map {|vm_hostname, vm_data| vm_data[:ip]}.join(",")
    end
```

* change `config.proxy.enabled` to true
* change `config.proxy.http` to the address of your HTTP proxy
* change `config.proxy.https` to the address of your HTTPS proxy

Finally, start the virtual machines

```
vagrant up --provision
```

## Acquiring the training's source code

* connect to the `provisioner` VM either by using the `vagrant ssh provisioner` command or by opening a graphical interface through VirtualBox GUI (user: vagrant, password: vagrant)

* open a terminal session with Terminator on `provisioner` (only if using the VirtualBox GUI method) and clone the training's repository
```
git clone https://github.com/goraje/ansibletraining.git
```

* enter the training's directory and create a Python virtual environment using pyenv
```
cd ansibletraining
pyenv virtualenv 3.8.3 ansible-training
pyenv local ansible-training
```

* install Ansible with `pip`
```
pip install ansible
```
