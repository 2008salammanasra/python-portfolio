#fix_the_rules.py
#This program checks a connection against three rules.
#1.requesting input from the user
role = input("Role: ")
#2. الخطا هو لم يتم التحويل لعدد صحيح ونوعه (runtime error: typeerror) ويرسل مسج خطا انه كان سيتوقف البرنامج في السطر الثاني لانه لا يمكن مقارنة نص مع رقم 
port = int(input("Port: "))
#3. هنا يتم تعديل علامة = الى == ليصبح كسؤال وليس لاسناد قيمة 
#3. ونوع الخطا خطا منطقي (logical error) ولن يرسل رسالة خطا ويعمل ولكن ستكون النتيجة خاطئة وتخرب المتغيرات 
is_admin = role == "admin"
#4. هنا تمت كتابة الرمز بالمقلوب ونوع الخطا (syntax error : invalid syntax ) ويرسل رسالة فورية قبل ان يبدا بالعمل 
is_system_port = port <= 1023
#5.هنا تم كتابة الرقم مباشرة بعد or دون كتابة كلمة port  قبلها لتكون العبارة صحيحة 
#5.ونوع الخطا  خطا منطقي ولن يرسل رسالة خطا لكنه سيعطي النتيجة بشكل خاطئ 
is_web_port = (port == 80) or (port == 443)
#6. وهذه اسطر الطباعة سوف تعمل دون اخطاء
print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")
