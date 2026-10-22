#fix_the_record.py
#this program prints a short record about a network device
device_name = "edge-router"
#1. syntaxerror:اسم المتغير لا يمكن ان يبدا برقم
second_ip = "192.0.2.1"
#2.syntaxerror: كلمة class محجوزة في بايثون ولا تستخدم كاسم متغير 
device_class = "router"
#3. runtimeerror (valueerror): لا يمكن تحويل الكلمات النصية الى ارقام ب int
port = int("22")
#runtimeerror (name error):تم تصحيح اسم المتغير باضافة حرف e في اخره
print("device:" , device_name)
print("backup ip:" , second_ip)
print("type:" , device_class)
print("port:" , port)
#اجابة السؤال الرابع اي الاخطاء تظهر بالاول 
#syntaxerror الاخطاء الصياغية هي التي تظهر بالاول لان بايثون يقرا ويفحص الكود للتاكد من قواعده قبل بدء التشغيل اي سطر 
