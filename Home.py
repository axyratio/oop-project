import streamlit as st
import pandas as pd
from component.Components import Component
#page 
class App:
    def __init__(self) -> None:
        pass

    def home(self):

        comp = Component()
        url = comp.read_url()
        
        tab1, tab2 = st.tabs(["Home", "Contact"])
        with tab1:
            st.title("My App")    
            st.markdown(f'''<span>Convert base numbers Can be converted from 2 - 16 <a href="{url}/ConvertBase">Click to Project</a></span>''', unsafe_allow_html=True)
            comp.comment()

        with tab2:
            st.header("Contact me")
            st.markdown("<ul><a href='https://www.facebook.com/12ize12'><li>Facebook me</li></a><a href='github.com/axyratio/'><li>Github</li></a></ul>", unsafe_allow_html=True)

            st.header("Donate")
            x = "[![banners](https://github.com/axyratio/axyratio.github.io/assets/159877997/5e9cda05-f772-405b-9544-909b772fb8d4)](https://www.buymeacoffee.com/kittiphong92)"
            st.markdown(x)

    def run(self):
        self.home()
    
if __name__ == "__main__":
    App().run()

