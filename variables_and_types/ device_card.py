#divice_card.py
#البرنامج يقوم بحفظ البيانات تجهاز شبكة وطباعتها وتحديثها
# تعريف الثابت باحرف كبيرة 
max_connections =100
#تعريف المتغيرات الاربعة 
device_name ="web-server-01"
device_ip = "192.0.2.20"
service ="https"
open_port = 443
#طباعة كل قيمة مع نص توضيحي
print("device:", device_name)
print("ip address:", device_ip)
print("service:", service)
print("port:",open_port)
print("max connections:", max_connections)
#تغيير قيمتين (الخدمة والمنفذ ) وطباعتها في سطر واحد
service = "ssh"
open_port = 22
print("updated service:", service ,"on port" , open_port)
