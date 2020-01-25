import json

def retjson(name, age):
    address = 'Banjar Wijaya B.50 No.12 Tangerang '
    hobbies = ['membaca', 'traveling', 'berenang']
    is_married = bool(False) #Isi True jika married, False jika Tidak
    list_school = []
    list_school.append({'name': 'SDN CIPONDOH 02', 'year_in' : '2001', 'year_out':'2007', 'major':None})
    list_school.append({'name': 'SMPN 1 TANGERANG', 'year_in': '2007', 'year_out': '2010', 'major': None})
    list_school.append({'name': 'SMAN 7 TANGRANG', 'year_in': '2010', 'year_out': '2013', 'major': 'IPA'})
    list_school.append({'name': 'TELKOM UNIVERSITY', 'year_in': '2013', 'year_out': '2013', 'major': 'TEKNIK INDUSTRI'})
    skills = []
    skills.append({'skill_name':'MICROSOFT EXCEL','level':'INTERMEDIATE'})
    interested_in_coding = bool(True) #Isi True jika tertarik ngoding, isi false jika gak tertarik
    dictProf = {'name': name, 'age': age, 'address': address, 'hobbies': hobbies, 'is_married': is_married, 'list_school': list_school, 'skills':skills}
    python2json = json.dumps(dictProf)
    print(python2json)
retjson("ARNUR HANIFA", 24)