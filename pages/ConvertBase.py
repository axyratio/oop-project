import streamlit as st
from streamlit_javascript import st_javascript
from PIL import Image
from component.Components import Component

class App():
    def run(self): 
        cp = Component()

        cp.updateParams()
        cp.inputBase()
        cp.moreBase()

            


if __name__ == "__main__":
    app = App()
    app.run()
    
    
    
    