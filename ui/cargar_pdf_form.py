# ui/cargar_pdf_form.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from processing.pdf_processor import procesar_archivo_pdf
from kivy.uix.popup import Popup

class CargarPDFForm(BoxLayout):
    def __init__(self, **kwargs):
        super(CargarPDFForm, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.add_widget(Label(text="Palabra clave"))
        self.palabra_clave_input = TextInput(multiline=False)
        self.add_widget(self.palabra_clave_input)

        self.file_chooser = FileChooserIconView(filters=['*.pdf'])
        self.add_widget(self.file_chooser)

        self.procesar_btn = Button(text="Procesar")
        self.procesar_btn.bind(on_press=self.procesar_pdf)
        self.add_widget(self.procesar_btn)

        btn_volver = Button(text='Volver')
        btn_volver.bind(on_press=self.volver)
        self.add_widget(btn_volver)
        
    # Este método se invoca cuando el botón 'Procesar' es presionado
    def procesar_pdf(self, instance):
        selected = self.file_chooser.selection
        palabra_clave = self.palabra_clave_input.text
        if selected:
            procesar_archivo_pdf(selected[0], palabra_clave)
            # Aquí no cierras el popup para permitir múltiples procesamientos si es necesario
        else:
            print("Por favor, seleccione un archivo PDF para procesar.")
    
    # Este método se invoca cuando el botón 'Volver' es presionado
    def volver(self, instance):
        # Cierra el Popup usando la referencia al 'Popup' almacenada
        if self.parent and isinstance(self.parent.parent, Popup):
            self.parent.parent.dismiss()

