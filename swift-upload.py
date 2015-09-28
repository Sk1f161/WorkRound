#!/usr/bin/python

import swiftclient

tenant_name='Swift'
user='richclip'
key='saifas0000'
authurl='https://openstack.richclip.com:35357/v2.0'
#export OS_IMAGE_API_VERSION=2
#export OS_VOLUME_API_VERSION=2

conn = swiftclient.Connection(
    user=user,
    key=key,
    authurl=authurl,
    tenant_name=tenant_name,
     auth_version='1'



)
print(conn)
for container in conn.get_account()[1]:
        print container['name']
