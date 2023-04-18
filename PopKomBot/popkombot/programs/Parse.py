import xml.etree.ElementTree as ET
import openpyxl


def creat_part(cb):

    tree = ET.parse(f'./{cb}/File.xml')
    root = tree.getroot()


    book = openpyxl.Workbook()
    sheet = book.active
    sheet.append(['Номер','Реплика','Время','Триггер','Информация'])
    sheet.column_dimensions['B'].width = 60
    sheet.column_dimensions['E'].width = 60




    list_final = []


    for elem in root.iter('{http://schemas.malighting.de/grandma2/xml/MA}Cue'):
        info = ''
        for i in elem:
            if i.tag == '{http://schemas.malighting.de/grandma2/xml/MA}InfoItems':
                info = i.find('{http://schemas.malighting.de/grandma2/xml/MA}Info').text


        for child in elem.iter('{http://schemas.malighting.de/grandma2/xml/MA}CuePart'):
            name = child.attrib.get('name', 'cue')
            numb = f"{elem.find('{http://schemas.malighting.de/grandma2/xml/MA}Number').get('number')}." \
                   f"{int(int(elem.find('{http://schemas.malighting.de/grandma2/xml/MA}Number').get('sub_number')) * 0.01)}" \
                if elem.find('{http://schemas.malighting.de/grandma2/xml/MA}Number').get('sub_number') != '0' \
                else elem.find('{http://schemas.malighting.de/grandma2/xml/MA}Number').get('number')
            trig = elem.find('{http://schemas.malighting.de/grandma2/xml/MA}Trigger').get('type') \
                if elem.find('{http://schemas.malighting.de/grandma2/xml/MA}Trigger') != None else 'Go'
            tim = child.attrib.get('basic_fade') if child.attrib.get('basic_fade') != None else "0"
            list_final.append([numb, name, tim, trig, info])
    print(list_final)



    for i in range(len(list_final)):
        sheet.append(list_final[i])






    book.save(f'./{cb}/Partitura.xlsx')








