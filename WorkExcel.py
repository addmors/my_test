from openpyxl import Workbook
from openpyxl.styles import Alignment


class Work(Workbook):
    def __init__(self):
        super().__init__()
        self.next = 0
        self.ws = None

    def next_list(self, name):
        self.ws = super().create_sheet(title=name, index=self.next)
        self.next += 1
        l = ['Ссылка', 'Заголовок', 'Описание', 'позиция']
        for i in range(3):
            self.ws.column_dimensions[chr(65+i)].width = 40
        self.ws.append(l)

    def append(self, ls):
        temp = []
        for i in range(len(ls[0])):
            for j in range(len(ls)):
                temp.append(str(ls[j][i]))
            temp.append(i+1)
            self.ws.append(temp)
            temp.clear()

        for row in self.ws.iter_rows():
            for cell in row:
                cell.alignment = Alignment(wrap_text=True, vertical='top', horizontal='center')

    def saving(self, name):
        super().save('%s.xlsx' % name)
