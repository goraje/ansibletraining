#!/bin/env python

import argparse
import json
import vagrant


class SampleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.get_args()

        if self.args.list:
            self.inventory = self.generate_inventory()
        elif self.args.host:
            self.inventory = self.get_empty_inventory()
        else:
            self.inventory = self.get_empty_inventory()
        
        print(json.dumps(self.inventory))
    
    def get_args(self):

        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store_true')
        self.args = parser.parse_args()
    
    def generate_inventory(self):

        new_inventory = {
            'all': {},
            '_meta':{
                'hostvars': {}
            }
        }

        v = vagrant.Vagrant()
        
        ansible_ssh_user = v.user()
        new_inventory['all']['vars'] = {'ansible_ssh_user': ansible_ssh_user}

        hosts = [host.name for host in v.status()]
        new_inventory['all']['hosts'] = hosts

        for host in hosts:
            ansible_host = v.hostname(host)
            ansible_port = v.port(host)
            new_inventory['_meta']['hostvars'][host] = {
                'ansible_host': ansible_host,
                'ansible_port': ansible_port
            }


        return new_inventory

    
    def get_empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

if __name__ == '__main__':
    SampleInventory()