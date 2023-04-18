

import openpyxl

from openpyxl.drawing.image import Image



def add_photo_preset_list(title: str, cb):
    boook = openpyxl.load_workbook(f'./{cb}/Preset.xlsx')
    sheet = boook.active
    logo = Image(f'./{cb}/Photo.jpg')
    logo.height = 240
    logo.width = 470
    list_preset = {}
    for i in range(2, sheet.max_row + 1):
        list_preset[sheet[f'A{i}'].value] = i
    sheet.add_image(logo, f'B{list_preset.get(title)}')
    print(list_preset)
    boook.save(f'./{cb}/Preset.xlsx')






