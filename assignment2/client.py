from ncclient import manager
import xml.dom.minidom

m = manager.connect(host='sandbox-iosxr-1.cisco.com', port='830',
                    username='admin', password='C1sco12345', device_params={'name': 'iosxr'})

print(m.connected)

# for capability in m.server_capabilities:
# print('*'*10)
# print(capability)

config = m.get_config('running').xml
print(xml.dom.minidom.parseString(config).toprettyxml())

with open("%s.xml" % 'sandbox-iosxr-1.cisco.com', 'w') as f:
    f.write(config)

m.close_session()
