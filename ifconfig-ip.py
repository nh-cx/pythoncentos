#Python学习专用
#
#
#
import os, re
ifcfg_result = os.popen('ifconfig').read()

print(ifcfg_result)

ip_list = re.findall('[1,2]?\d?\d+\.[1,2]?\d?\d+\.[1,2]?\d?\d+\.[1,2]?\d?\d', ifcfg_result)

str_mac = re.search('(\w\w:+\w\w:+\w\w:+\w\w:+\w\w:+\w\w)', ifcfg_result).groups()[0]


ipadd = ''
ipmask = ''
ipboradcast = ''

# 方法1
# for x in ip_list:
#     if x == '127.0.0.1' or x == '255.0.0.0' :
#         pass
#     else:
#         if re.match('(.*)\.(.*)\.(.*)\.(.*)',x).groups()[3] == '0' :
#             ipmask = x
#         elif re.match('(.*)\.(.*)\.(.*)\.(.*)',x).groups()[3] == '255' :
#             ipboradcast = x
#         else:
#             ipadd = x

# 方法2
for x in ip_list:
    if x == '127.0.0.1' or x == '255.0.0.0' :
        pass
    else:
        if re.split('\.', x)[3] == '0' :
            ipmask = x
        elif re.split('\.', x)[3] == '255' :
            ipboradcast = x
        else:
            ipadd = x

# 方法3
# for x in ip_list:
#     if x == '127.0.0.1' or x == '255.0.0.0' :
#         pass
#     else:
#         if str(x).split('.')[3] == '0' :
#             ipmask = x
#         elif str(x).split('.')[3]  == '255' :
#             ipboradcast = x
#         else:
#             ipadd = x

str_print = '{0}\n{1:12}:{2:20}\n{3:12}:{4:20}\n{5:12}:{6:20}\n{7:12}:{8:20}\n{9}'.format('-'*60, r'IPADDRESS', ipadd, r'NETMASK', ipmask, r'BROADCAST', ipboradcast, 'MAC ADDRESS', str_mac, '-'*60)
print(str_print)
