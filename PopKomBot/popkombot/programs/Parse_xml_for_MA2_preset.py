import xml.etree.ElementTree as ET
import openpyxl

from openpyxl.styles import Font


def create_presets(cb):



    tree = ET.parse(f'./{cb}/File.xml')
    root = tree.getroot()
    book = openpyxl.Workbook()
    sheet = book.active
    sheet.append(['Название пресета','Фото','Описание'])
    sheet.column_dimensions['A'].width = 60
    sheet.column_dimensions['C'].width = 60
    sheet.column_dimensions['B'].width = 70
    sheet['A1'].font = Font(size=23, color= 'ff0000')
    sheet['B1'].font = Font(size=23, color= 'ff0000')
    sheet['C1'].font = Font(size=23, color= 'ff0000')



    list_preset = []


    for elem in root.iter('{http://schemas.malighting.de/grandma2/xml/MA}Preset'):
        if elem.attrib.get('name') not in list_preset:
            list_preset.append(elem.attrib.get('name'))







    for i in range(len(list_preset)):
        sheet.append([list_preset[i]])
        sheet[f'A{i + 2}'].font = Font(size=23)
        sheet.row_dimensions[i + 2].height = 200
    print(list_preset)





    book.save(f"./{cb}/Preset.xlsx")






