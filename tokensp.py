#!/usr/bin/env python3
import re

##Разбивает на части по INSERT
#f = open('token.sql','r').read()
#fs = f.split('INSERT')
#print(len(fs))
#print(fs[9])
# col=0
# for sfs in fs:
#t=open('res_end','w')
#t.write(fs[9])
#t.close()
#     col = col+1

##Меняем строку в файле
f = open('res_endr8','r').read()
fr = open('res_endr9','w')
### User name
#fr.write(re.sub(r'\"admin\\',r'"richclip\\',f))
### Tanant Description
fr.write(re.sub('Admin Tenant','ObjectStorage',f))
### User Admin to user richclip
#fr.write(re.sub('7b793973f9f240139dcd365ae453d60b','dc6955c24e2d4d48883464e3d80ba2bf',f))
### Project demo
#fr.write(re.sub('252ebf2b9b264592834b3900b9a96004','11607d536b28414fbf2eb21142bfb312',f))
### Role Admin
#fr.write(re.sub('4a0bb418e0e54e09ac6eec63bbc1cc84','46d9f6ebf6e647f29c39968561ef27a5',f))
### Endpoint
#fr.write(re.sub('Germany','Falkenstein',f))
### Change URL keystone
#fr.write(re.sub('swiftde.saifas.com:35357','openstack.richclip.com:35357',f))
### Change AUTH URL keystone
#fr.write(re.sub('swiftde.saifas.com:5000','openstack.richclip.com:5000',f))
### Chande id Endpoint for 35357
#fr.write(re.sub('c0782b4fc148498aa7b8a4f49ece523e','b7b2b510884147e78032a9896763a74a',f))
### Change id Endpoint for 8080
#fr.write(re.sub('083108a115414a06acd7bf52942cd246','f2ce9bab2d324515905bb508ad920431',f))
