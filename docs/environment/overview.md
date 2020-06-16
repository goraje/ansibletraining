# Overview

The training environment consists of 3 virtual machines hosted by a local VirtualBox hypervisor. Generation of the virtual machines is automated with Vagrant.

A short description of the virtual machines:

!!! info "vm_name: provisioner"
    ```yaml
    platform: linux
    os: CentOS 7
    vagrant_box: goraje/centos7-xfce
    graphical_environment: true
    role: provisioner
    ```

    The goal of the training is to make it easily accessible to users of all system platforms. Since Ansible installation is broken for Windows hosts the training environment provides a VM that will act as the provisioning host. The VM includes a graphical interface (XFCE) and basic utilities: git, terminator, firefox and gedit.

!!! info "vm_name: centos1"
    ```yaml
    platform: linux
    os: CentOS 7
    vagrant_box: centos/7
    graphical_environment: false
    role: remote host
    ```

    This VM will act as a hypothetical remote host.

!!! info "vm_name: ubuntu1"
    ```yaml
    platform: linux
    os: Ubuntu 18.04
    vagrant_box: ubuntu/bionic64
    graphical_environment: false
    role: remote host
    ```

    This VM will act as a hypothetical remote host.
