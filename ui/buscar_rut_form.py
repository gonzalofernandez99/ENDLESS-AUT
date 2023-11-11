from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from processing.rut_processor import procesar_rut

class BuscarRUTForm(BoxLayout):
    def __init__(self, **kwargs):
        super(BuscarRUTForm, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.add_widget(Label(text="Nombre"))
        self.nombre_input = TextInput(multiline=False)
        self.add_widget(self.nombre_input)

        self.add_widget(Label(text="Apellido"))
        self.apellido_input = TextInput(multiline=False)
        self.add_widget(self.apellido_input)
        
        self.add_widget(Label(text="Empresa"))
        self.empresa_input = TextInput(multiline=False)
        self.add_widget(self.empresa_input)

        self.enviar_btn = Button(text="Enviar")
        self.enviar_btn.bind(on_press=self.enviar_informacion)
        self.add_widget(self.enviar_btn)

        btn_volver = Button(text='Volver')
        btn_volver.bind(on_press=self.volver)
        self.add_widget(btn_volver)

    def enviar_informacion(self, instance):
        nombre = self.nombre_input.text
        apellido = self.apellido_input.text
        empresa = self.empresa_input.text
        procesar_rut(nombre, apellido, empresa)  # Asumiendo que procesar_rut() no necesita cerrar el popup.
        # No cierre el Popup aquí si quieres enviar múltiples veces sin cerrar el formulario.

    def volver(self, instance):
        # Suponiendo que 'volver' es llamado por un botón dentro de un Popup, se cierra el Popup.
        # Esta es la referencia al Popup que contiene este BoxLayout.
        popup = self.parent.parent  # El padre del BoxLayout (este formulario) es el contenido del Popup, y el padre de eso debería ser el Popup.
        if isinstance(popup, Popup):
            popup.dismiss()

