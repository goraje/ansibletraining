#!/bin/env python

import json
import argparse

class SampleInventory:

    HOSTS = [
        {
            "host": "provisioner",
            "vars": {
                'ansible_connection': 'local'
            }
        },
        {
            "host": "centos1",
            "vars": {
                "ansible_host": "192.168.77.22",
                "ansible_port": 2345
            }
        },
        {
            "host": "ubuntu1",
            "vars": {
                "ansible_host": "192.168.77.23"
            }
        }
    ]

    GROUPS = [
        {
            "name": "centos",
            "hosts": ["provisioner", "centos1"],
            "vars": {
                "ansible_become": True
            }
        },
        {
            "name": "ubuntu",
            "hosts": ["ubuntu1"]
        }
    ]

    def generate_response(self, parser):
        args = parser.parse_args()
        if args.list and args.host is None:
            self.get_list()
        elif not args.list and args.host:
            self.get_host(args.host)
        else:
            parser.print_help()

    def get_host(self, host):
        try:
            host_data = [x for x in self.HOSTS if x["host"] == host][0]
            print(json.dumps(host_data["vars"], indent=4))
        except IndexError as e:
            raise IndexError('Host not found.')

    def get_list(self):
        inventory = {}
        meta = self.create_meta()
        groups = self.create_groups()
        inventory.update(meta)
        inventory.update(groups)
        print(json.dumps(inventory, indent=4))

    def create_meta(self):
        meta = {
            "_meta": {
                "hostvars": {}
            }
        }
        for host in self.HOSTS:
            all_vars = {}
            host_hostvars = host["vars"]
            host_groupvars = self.get_host_groupvars(host)
            all_vars.update(host_hostvars)
            all_vars.update(host_groupvars)
            meta["_meta"]["hostvars"][host["host"]] = all_vars
        return meta

    def get_host_groupvars(self, host):
        group_vars = {}
        for group in self.GROUPS:
            if host["host"] in group["hosts"]:
                try:
                    group_vars.update(group["vars"])
                except KeyError:
                    pass
        return group_vars

    def create_groups(self):
        groups = {
            "all": {
                "children": ["ungrouped"]
            }
        }
        for group in self.GROUPS:
            groups[group["name"]] = group["hosts"]
            groups["all"]["children"].append(group["name"])
        return groups

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action = 'store_true')
    parser.add_argument('--host')
    SampleInventory().generate_response(parser)
