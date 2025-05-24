import tika
from tika import parser
import re

file = r'C:\Users\SSLTP11373\Downloads\demo2.pdf'
#file = r'C:\Users\SSLTP11373\Downloads\JGOKULNATH_PHP developer_Bangalore.pdf'
#file = r'C:\Users\SSLTP11373\Downloads\Harish PAndian_Cv_06072021_1040 (1).pdf'
#file = r'C:\Users\SSLTP11373\Desktop\parser\Preethi.pdf'
#file = r'C:\Users\SSLTP11373\Desktop\parser\raji_resume.pdf'

#file = r'C:\Users\SSLTP11373\Desktop\parser\Resume_of_a_Trainee_Akash.pdf'
#file = r'C:\Users\SSLTP11373\Desktop\parser\Vicky_Pyspark_1.pdf'
#file = r'C:\Users\SSLTP11373\Desktop\parser\AyonaSumonBaby_PHP Developer_Bangalore.pdf'
#file = r'C:\Users\SSLTP11373\Desktop\parser\Radhikakulkarni_C++ Dicom_Pune.pdf'
#file = r'C:\Users\SSLTP11373\Desktop\parser\Yokeshwaran_MS SQL_Chennai.pdf'
#file = r'C:\Users\SSLTP11373\Desktop\parser\PDURGAPRASAD_Oracle DBA_Bangalore.pdf'
#file = r'C:\Users\SSLTP11373\Desktop\parser\NagendraPrasad_Salesforce_Bangalore.pdf'


file_data = parser.from_file(file)

u_text = file_data['content']
j = u_text.split("\n")
print(j)