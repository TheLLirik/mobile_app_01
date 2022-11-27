
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import webbrowser

google_search = "https://api.track24.ru/tracking.json.php?apiKey=af2ba9fbe97492f15cd194c7652e4432&domain=google.com&pretty=true&code={}"
class Float_layot_Demo(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.l=Label(
            text="Введите ваш трек-код!",
            size_hint=(1, 0.8),
            pos_hint={"x": 0, 'y': 0.2}
        )
        self.add_widget(self.l)
        self.t = TextInput(
            size_hint = (0.8, 0.05),
            pos_hint = {"x":0, "y": 0}
        )
        self.add_widget(self.t)
        self.btn = Button(
            text = "Send",
            size_hint = (0.2, 0.05),
            pos_hint = {"x":0.8, "y":0}
        )
        self.btn.fbind('on_press', lambda x: self.GoogleSearch())
        self.add_widget(self.btn)

    def GoogleSearch(self):
        msg = self.t.text
        print(msg)
        webbrowser.open(google_search.format(msg))
        self.t.text = ""


class DemoApp(App):
    def build(self):
        layout = AnchorLayout(
            anchor_x='right',
            anchor_y='bottom'

        )
        button=Button(
            text = 'send',
            size_hint=(.2,.1),
            background_color=(0.1,25,86,1),
            color=(0,0,0,1)

        )
        layout.add_widget(button)
        #return layout
        return Float_layot_Demo()

demo=DemoApp()
demo.run()