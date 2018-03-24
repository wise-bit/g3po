# kivy imports

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# biopython imports

from Bio import Entrez


class bioo():

    def dna_sequence(name):

        organism_name = name

        try:
            Entrez.email = "a@example.com" 
            handle = Entrez.esearch(db="nucleotide", term=organism_name)
            record = Entrez.read(handle)
            for i in range(20):
                select = record["IdList"][i]
                handle = Entrez.efetch(db="nucleotide", id=select, rettype="gb", retmode="xml")

                h = handle.read()
                hh = h.split("<GBSeq_sequence>")[1].split("</GBSeq_sequence>")

                if len(hh[0]) < 2000:
                    return hh[0]
                    break
                if i == 19:
                    print("not found. Please try again")
                    break

                handle.close()

        except:
            return "Unexpected error. Please check input or try again later"


class MyDnaApp(BoxLayout): 

    def __init__(self, **kwargs):

        bio  = bioo()

        super(MyDnaApp, self).__init__(**kwargs)
        self.orientation = "vertical"

        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))

        my_output = Label(text="DNA value appears here",
                              text_size=(None,None),
                              font_size="20sp",
                              size = self.size,
                              halign="center",
                              valign = "middle",
                              color=(0.901, 0.901, 0.901, 1))

        my_output.bind(size=my_output.setter('text_size'))

        root.add_widget(my_output)
        self.add_widget(root)

        my_user_input = TextInput(size_hint_y=None)
        self.add_widget(my_user_input)

        def callback(value):
            vaal = bioo.dna_sequence(value)
            my_output.text = vaal

        def callback2(instance):
            # my_user_input.bind(text=callback)
            callback(my_user_input.text)

        button = Button(text='Fetch results', font_size=18, 
                              size_hint_y=None)
        self.add_widget(button)

        button.bind(on_press=callback2)

        


class DNAFractalApp(App):

    def build(self):
        return MyDnaApp()


if __name__ == '__main__':
    DNAFractalApp().run()