import pip._vendor.requests
import parsel
import os
import stat
dict_ip_name={}
ip_name=[]
name_list=[]
ip_list=[]
hosts_lines=[]
for i in range(0,2):
    webpage = ['github.global.ssl.fastly.net','github.com']
    base_url='https://websites.ipaddress.com/{}'.format(webpage[i])
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    response = pip._vendor.requests.get(base_url,headers=headers)
    data = response.text
    ip_information = parsel.Selector(data)
    parsel_ip=ip_information.xpath('//ul[@class="comma-separated"]/li')
    parsel_name=ip_information.xpath('//div[@class="resp main"]/main/h1')
    for li in parsel_ip:
        ipadress = li.xpath('text()').extract_first()
        break
    for h1 in parsel_name:
        name = h1.xpath('text()').extract_first().lower()
    dict_ip_name.update({ipadress:name})
os.chmod('C:/Windows/System32/drivers/etc/hosts',stat.S_IWRITE)
hostsfile = open('C:/Windows/System32/drivers/etc/hosts','r',encoding='utf-8-sig').readlines()
for name_in_dict in dict_ip_name.values():
    name_list.append(name_in_dict.lower())
for hosts_line in hostsfile:
    if hosts_line[0]=="#":
        hosts_lines.append(str(hosts_line))
    else:
        if hosts_line.strip()!='':
            ip_in_hosts = hosts_line.strip().split()[0]
            name_in_hosts = hosts_line.strip().split()[1].lower()
            if name_in_hosts in name_list:
                cur_key=list (dict_ip_name.keys()) [list (dict_ip_name.values()).index (name_in_hosts)]
                hosts_line = cur_key + ' ' + name_in_hosts
                hosts_lines.append(str(hosts_line))
                dict_ip_name.pop(cur_key)
            else:
                hosts_lines.append(str(hosts_line))
for key in dict_ip_name:
    hosts_line = key + ' ' + dict_ip_name[key]
    hosts_lines.append(hosts_line)
whostsfile = open(r'C:/Windows/System32/drivers/etc/hosts','w')
for i in range(0,len(hosts_lines)):
    whostsfile.write('\n'+hosts_lines[i])
whostsfile.close()
print('successful')


    


