import wx
from LR_18 import SuperMarketDatabase, SaleOfGoods
from Term import SuperMarketTerm


class SuperMarketGUI(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Supermarket', size=(500, 250))
        self.term = SuperMarketTerm()

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox_db = wx.BoxSizer(wx.HORIZONTAL)
        label_db = wx.StaticText(panel, label='Database:')
        hbox_db.Add(label_db, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)
        self.text_db = wx.TextCtrl(panel, value=self.term.db_file)
        hbox_db.Add(self.text_db, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)
        vbox.Add(hbox_db, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        hbox_goods = wx.BoxSizer(wx.HORIZONTAL)
        label_goods = wx.StaticText(panel, label='Goods:')
        hbox_goods.Add(label_goods, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)
        self.text_goods = wx.TextCtrl(panel)
        hbox_goods.Add(self.text_goods, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)
        vbox.Add(hbox_goods, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        hbox_seller = wx.BoxSizer(wx.HORIZONTAL)
        label_seller = wx.StaticText(panel, label='Seller:')
        hbox_seller.Add(label_seller, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)
        self.text_seller = wx.TextCtrl(panel)
        hbox_seller.Add(self.text_seller, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)
        vbox.Add(hbox_seller, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        hbox_count = wx.BoxSizer(wx.HORIZONTAL)
        label_count = wx.StaticText(panel, label='Count:')
        hbox_count.Add(label_count, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)
        self.text_count = wx.TextCtrl(panel)
        hbox_count.Add(self.text_count, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.BOTTOM, border=5)
        vbox.Add(hbox_count, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        hbox_buttons = wx.BoxSizer(wx.HORIZONTAL)
        self.button_add = wx.Button(panel, label='Add')
        hbox_buttons.Add(self.button_add, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM, border=5)
        self.button_delete = wx.Button(panel, label='Delete')
        hbox_buttons.Add(self.button_delete, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM, border=5)
        self.button_print = wx.Button(panel, label='Print')
        hbox_buttons.Add(self.button_print, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM, border=5)
        self.button_save = wx.Button(panel, label='Save')
        hbox_buttons.Add(self.button_save, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM, border=5)
        self.button_delete_db = wx.Button(panel, label='Delete DB')
        hbox_buttons.Add(self.button_delete_db, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM, border=5)
        self.button_exit = wx.Button(panel, label='Exit')
        hbox_buttons.Add(self.button_exit, flag=wx.LEFT|wx.RIGHT|wx.BOTTOM, border=5)
        vbox.Add(hbox_buttons,flag=wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, border=5)

        self.Bind(wx.EVT_BUTTON, self.on_add, self.button_add)
        self.Bind(wx.EVT_BUTTON, self.on_delete, self.button_delete)
        self.Bind(wx.EVT_BUTTON, self.on_print, self.button_print)
        self.Bind(wx.EVT_BUTTON, self.on_save, self.button_save)
        self.Bind(wx.EVT_BUTTON, self.on_delete_db, self.button_delete_db)
        self.Bind(wx.EVT_BUTTON, self.on_exit, self.button_exit)

        panel.SetSizer(vbox)

    def on_add(self, event):
        goods = self.text_goods.GetValue()
        seller = self.text_seller.GetValue()
        count = int(self.text_count.GetValue())

        if goods and seller and count:
            sale = SaleOfGoods(goods, seller, count)
            self.term.supermarket_database.add_sale(sale)
            wx.MessageBox('Sale added successfully.', 'Success')
            self.text_goods.SetValue('')
            self.text_seller.SetValue('')
            self.text_count.SetValue('')
        else:
            wx.MessageBox('Please fill all the fields.', 'Error')

    def on_delete(self, event):
        # Создаем диалоговое окно для ввода индекса элемента
        dlg = wx.TextEntryDialog(self, 'Enter the index of the item to delete:', 'Delete Item')
        if dlg.ShowModal() == wx.ID_OK:
            try:
                # Получаем индекс элемента из диалогового окна
                index = int(dlg.GetValue())
                # Удаляем элемент по индексу из базы данных
                sales = self.term.supermarket_database._sales
                sale_to_delete = sales[index]
                self.term.supermarket_database.remove_sale(sale_to_delete)
                wx.MessageBox('Sale deleted successfully.', 'Success')
            except ValueError:
                wx.MessageBox('Invalid index value.', 'Error', wx.OK | wx.ICON_ERROR)
        dlg.Destroy()

    def on_print(self, event):
        sales = self.term.supermarket_database.get_sales()
        wx.MessageBox('\n'.join('Sale of {0} by {1}, count: {2}'.format(s.goods, s.seller, s.count) for s in sales), 'Sales')

    def on_save(self, event):
        self.term.supermarket_database.save_database(self.text_db.GetValue())
        wx.MessageBox('Sales saved successfully.', 'Success')

    def on_delete_db(self, event):
        self.term.supermarket_database.delete_database(self.text_db.GetValue())
        wx.MessageBox('Database deleted successfully.', 'Success')

    def on_exit(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    gui = SuperMarketGUI()
    gui.Show()
    app.MainLoop()
