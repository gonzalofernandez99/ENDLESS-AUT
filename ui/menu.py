# ui/menu.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from ui.buscar_rut_form import BuscarRUTForm
from ui.cargar_pdf_form import CargarPDFForm

class MenuPrincipal(BoxLayout):
    def __init__(self, **kwargs):
        super(MenuPrincipal, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Botón Buscar RUT
        btn_buscar_rut = Button(text='Buscar RUT')
        btn_buscar_rut.bind(on_press=self.abrir_buscar_rut_form)
        self.add_widget(btn_buscar_rut)
        
        # Botón Cargar PDF
        btn_cargar_pdf = Button(text='Cargar PDF')
        btn_cargar_pdf.bind(on_press=self.abrir_cargar_pdf_form)
        self.add_widget(btn_cargar_pdf)

    def abrir_buscar_rut_form(self, instance):
        form = BuscarRUTForm()
        self.popup = Popup(title="Buscar RUT", content=form, size_hint=(0.9, 0.9))
        form.popup = self.popup  # Asignar referencia del popup al formulario
        self.popup.open()

    def abrir_cargar_pdf_form(self, instance):
        form = CargarPDFForm()
        self.popup = Popup(title="Cargar PDF", content=form, size_hint=(0.9, 0.9))
        form.popup = self.popup  # Asignar referencia del popup al formulario
        self.popup.open()

class MyApp(App):
    def build(self):
        return MenuPrincipal()

if __name__ == '__main__':
    MyApp().run()
