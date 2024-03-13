import streamlit as st
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