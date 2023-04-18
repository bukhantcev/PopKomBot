import openpyxl

def get_list_preset(index: int, cb):
    book = openpyxl.load_workbook(f'./{cb}/Preset.xlsx', keep_vba=True)
    sheet = book.active
    return sheet[f'A{index}'].value




