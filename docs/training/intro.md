# Before we begin

## Why Ansible?

* it's open-source
* written in Python
* no agent installation is required on the remote hosts
* acts primarily through SSH
* multiple built-in modules
* highly customizable through custom modules, callbacks etc.
* supports various levels of complex templating

## How does Ansible work?

Basically, Ansible works by connecting to the remote hosts through SSH and pushing small executable programs, which contain the desired definition of state on the remote. After execution, the programs are removed from the provisioned hosts.


## Are there any special requirements for Ansible to work?

In theory there are none, however

* since Ansible requires an SSH connection in order to send the executable code to the remotes, the user needs to provide a working and stable connection from the provisioning machine to the remote hosts
* under the hood Ansible executes the code on the remote hosts with Python so a working Python installation is required (in case Ansible does not detected a Python installation it will try to install Python via the `raw` module)
