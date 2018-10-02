#!/usr/bin/python

import traceback
import ldap.modlist
import ldap
import ldap.sasl

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.six import string_types
from ansible.module_utils_text import to_native, to_bytes



ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: add_remove_ldap_entry

short_description: This  module add/remove ldap entries.

version_added: "2.4"

description:
    - "This is my longer description explaining my sample module"

options:
    name:
        description:
            - This is the message to send to the sample module
        required: true
    new:
        description:
            - Control to demo if the result of this module is changed or not
        required: false

extends_documentation_fragment:

author:
    - Idan Kedmy (@yourhandle)
'''

EXAMPLES = '''
# Pass in a message
- name: Test with a message
  my_new_test_module:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_new_test_module:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_new_test_module:
    name: fail me
'''

RETURN = '''
original_message:
    description: The original name param that was passed in
    type: str
message:
    description: The output message that the sample module generates
'''

def main():
    module = AnsibleModule(
        argument_spec={
            'dn': dict(required=True),
            'state': dict(default='present', choices=['present', 'absent']),
            'server_uri': dict(default='ldapi:///'),
            'start_tls': dict(default='false', choices=(list(BOOLEANS)+['True', True, 'False', False])),
            'bind_dn': dict(default=None),
            'bind_pw': dict(default='', no_log=True),
        },
        check_invalid_arguments=False,
        supports_check_mode=True,
    )

state = module.params['state']






class LdapEntry(object):
    _connection = None

    def __init__(self, module):
        self.module = module

ldap = LdapEntry(module)
 if state == 'present':
     action = ldap.add()

self.module.params['attributes']['objectClass'] = (self.module.params['objectClass'])

if self.module.params['state'] == 'present':
    self.attrs = self._load_attrs()

def _load_attrs(self)
   attrs = {}

   for name, value in self.module.params['attributes'].items():
       if name not in attrs:
           attrs[name] = []
     
       if isinstance (value, list):
           attrs[name] = list(map(to_bytes, value))
       else
           attrs[name].append(to_bytes(value))
   
   return attrs


def add(self):
    def _add():
        self.connection.add_s(self.dn, modlist)
    if not self.is_entry_present():
        modlist = ldap.modlist.addModlist(self.attrs)
        action = _add
    else
        action = none
    return action


def is_entry_present(self):
    try:
        self.connection.search_s(self.dn, ldap.SCOPE_BASE)
    except ldap.NO_SUCH_OBJECT:
        is_present = False
    else:
        is_present = True

    return is_present

def connection(self):
    if self._connection is None:
        self._connection = self._connect_to_ldap()

    return self._connection

def _connect_to_ldap(self):
    connection = ldap.initialize(self.server_uri)

if __name__ == '__main__':
    main()
