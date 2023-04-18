import openpyxl
from openpyxl.styles import Font

def add_info_preset_list(title: str, text: str, cb):
    book = openpyxl.load_workbook(f'./{cb}/Preset.xlsx', keep_vba=True)
    sheet = book.active
    dict_preset = {}
    for i in range(2, sheet.max_row + 1):
        dict_preset[sheet[f'A{i}'].value] = i

    sheet[f'C{dict_preset.get(title)}'] = text
    sheet[f'C{dict_preset.get(title)}'].font = Font(size= 23)
    book.save(f"./{cb}/Preset.xlsx")







