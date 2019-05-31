# COURSE ENVIRONMENT SETUP

## Requirements

- Python
- Ansible
- VirtualBox
- Vagrant

## Installation - Linux Users

### Python

There is no need to follow any additional procedures since Python is installed by default on Linux distributions. To keep a clean working environment the user can setup a virtualenv using either: virtualenv, pipenv or pyenv. The choice is completely up to the user.

### Ansible

```shell
pip install ansible
```

### VirtualBox

```shell
#CentOS
sudo yum install -y epel-release
sudo yum install -y kernel-devel kernel-headers gcc make perl wget
wget https://www.virtualbox.org/download/oracle_vbox.asc
sudo rpm --import oracle_vbox.asc
sudo  wget http://download.virtualbox.org/virtualbox/rpm/el/virtualbox.repo -O /etc/yum.repos.d/virtualbox.repo
sudo yum install -y VirtualBox-6.0

#Fedora
sudo wget http://download.virtualbox.org/virtualbox/rpm/fedora/virtualbox.repo -P /etc/yum.repos.d/
sudo dnf update
sudo dnf install @development-tools
sudo dnf install kernel-devel kernel-headers dkms qt5-qtx11extras  elfutils-libelf-devel zlib-devel
sudo dnf install -y VirtualBox-6.0

#Ubuntu
sudo apt-get update
sudo apt install virtualbox

#Debian
echo "deb http://download.virtualbox.org/virtualbox/debian stretch contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
sudo apt-get update
sudo apt-get install virtualbox-6.0

#Archlinux family (Manjaro, Antegros etc.)
sudo pacman -S virtualbox
```

### Vagrant

```shell
#CentOS
wget https://releases.hashicorp.com/vagrant/2.2.4/vagrant_2.2.4_x86_64.rpm
sudo yum –y localinstall vagrant_2.2.2_x86_64.rpm

#Fedora
sudo dnf -y install vagrant

#Ubuntu
sudo apt install vagrant

# Archlinux family (Manjaro, Antegros etc.)
sudo pacman -S vagrant
```

## Installation - Windows Users

### Python

You can follow the installation instructions given at [this site](https://docs.python.org/3/using/windows.html). Remember to mark the option to "Add Python to PATH" at the beginning of the installation process. It will save you the time of adding it manually later.

### Ansible

```shell
pip install ansible
```

### VirtualBox

Download and install the binary package from the [official site](https://www.virtualbox.org/wiki/Downloads).

### Vagrant

Download and install the binary package from the [official site](https://www.vagrantup.com/downloads.html).

>**NOTE**: Vagrant requires Windows PowerShell version >= 3.0 to work correctly. This is of no concern for Windows 10 users, because the distribution comes with the software already installed on the system. However, Windows 7 users will need to download and install Windows Management Framework >= 3.0.

The newest version of Windows Management Framework available for Windows 7 SP1 or later can be found at the [official site](https://www.microsoft.com/en-us/download/details.aspx?id=54616).

## Environment setup

The definitions of the VMs that will be used during the training are located in the [Vagrantfile](Vagrantfile) in the top directory of the project.

In order to create and provision the VM's open your Linux terminal/Windows PowerShell and navigate to the project's top directory and execute:

```shell
vagrant up
```

This will download Vagrant's VM images (called boxes) and run them using VirtualBox.

>**NOTE**: If you are working behind a proxy environment don't forget to ensure that proxy is enabled for your Linux terminal/Windows PowerShell.

```shell
# Linux
export http_proxy=<proxy-url>:<port>
export https_proxy=<proxy-url>:<port>

# Windows
SET HTTP_PROXY=<proxy-url>:<proxy-port>
SET HTTPS_PROXY=<proxy-url>:<proxy-port>
```

A few useful commands:

```shell
# List deployed VMs and show their statuses
vagrant status

# Halt a deployed VM
vagrant halt VM_NAME

# Delete the deployed VMs
vagrant destroy
```
