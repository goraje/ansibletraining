# First steps

## Basic project layout

A basic Ansible project contains only the `inventory` file, which contains the metadata about the remote hosts and is necessary for Ansible to work. A simple representation of our current training environment could be depicted by the following `inventory`:

```ini
# hosts.ini
[centos]
provisioner     ansible_connection=local
centos1         ansible_host=192.168.77.22

[ubuntu]
ubuntu1         ansible_host=192.168.77.23
```

!!! note
    `Inventory` files are commonly named `hosts.<file_extenstion>`.

Another component that is commonly found in Ansible environments is the configuration file eg.:

```ini
#ansible.cfg
[defaults]
inventory = hosts.ini
host_key_checking = False
deprecation_warnings = False
```

The configuration file stores various options that are responsible for different aspects of Ansible's behavior. You can check the list of configurable settings in the [official documentation](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings-locations).

## Configuration file hierarchy

Ansible's configuration files can be stored in different locations, but only a single one will be used during Ansible execution.

Let's make a simple experiment:

* open a terminal session on the `provisioner`/SSH connection to the `provisioner` and enter the training directory
```
cd ansibletraining
```

* create a temporaty directory
```
mkdir temp
```

* inside this temporary directory create a `hosts.ini` file and copy the contents of the `inventory` mentioned in the previous section
```
cd temp
# then create hosts.ini with a text editor of your choice
```

* create an `ansible.cfg` in the same manner

* execute the following chain of commands
```
xargs -n 1 cp -v ansible.cfg<<<"/home/vagrant/ANSIBLE.cfg /home/vagrant/.ansible.cfg"
sudo mkdir -p /etc/ansible
sudo cp ansible.cfg /etc/ansible
export ANSIBLE_CONFIG=$HOME/ANSIBLE.cfg
```

* run `ansible --version` and find the value of `config file`

* execute `unset ANSIBLE_CONFIG` and repeat the previous process

!!! important
    If we continued with this chain of thought the result would yield the following precedence of configuration file locations:

    * `ANSIBLE_CONFIG` environment variable
    * `ansible.cfg` in the current directory
    * `~/.ansible.cfg` in the home directory
    * `/etc/ansible.cfg` systemwide Ansible configuration

## Testing the connectivity

As previously established Ansible works by pushing executable code through SSH. Connectivity to remote hosts can be tested using the `ping` module. Inside the `temp` directory execute:

```
ansible all -m ping
```

??? question "What is the expected result of the command?"
    Only `provisioner` will be reachable since we have not set up SSH connectivity to the remote hosts.

??? bug "Bonus round"
    Fix the problems with connectivity by creating a SSH keypair and copying the SSH public key to the remotes.

    * generate a new SSH key pair on `provisioner` (accept all prompts)
    ```
    ssh-keygen -C ""
    ```

    * copy the generated private key to `centos1` and `ubuntu1` (the SSH password is `vagrant` in both cases)
    ```
    ssh-copy-id -i ~/.ssh/id_rsa.pub vagrant@192.168.77.22
    ssh-copy-id -i ~/.ssh/id_rsa.pub vagrant@192.168.77.23
    ```

    * run the connectivity check once more
    ```
    ansible all -m ping
    ```
