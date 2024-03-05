import streamlit as st
from component.BaseConverter import BaseConverter
from urllib.parse import urlparse


class Component:
    # params
    def __init__(self, start_params=2, last_params=2) -> None:
        self.start_params = start_params
        self.last_params = last_params
    
    # call BaseConverter class to convert that users input.
    def converter(self, number=None, from_base=None, to_base=None, btn_onclick=None):
        # Validate inputs and perform conversion
        if btn_onclick:
            if not number:
                st.error("Please enter a number.")
            else:
                # convert เลขฐาน
                try:
                    converter = BaseConverter(number, from_base, to_base)
                    converted_number = converter.getBaseResult()
                    st.success(f"{converted_number}")
                # ถ้าใส่เลขที่ไม่มีใน เลขฐานที่เลือก
                except ValueError as e:
                    st.error(f"{number} is not in base {from_base}")

    def get_domain(url):
        # Extract the domain from the URL
        parsed_url = urlparse(url)
        return parsed_url.netloc
    
    # แนะนำเลขฐานอื่นๆ
    def moreBase(self, last_params=None, start_params=None):

        # return markdown tag
        def create_clickable_link(text, key):
            link = f'http://oop-project.streamlit.app/ConvertBase/?convert_from={key}'
            # Create a clickable link
            return f"[{text}]({link})"

        st.write("More to convert:")

        col1, col2, col3 = st.columns(3)
        
        with col1:
            links = [create_clickable_link(f"From base {i} to base {self.last_params}", f"{i}-to-{self.last_params}") for i in range(2,17) if self.last_params != i]
            st.markdown("<br>".join(links), unsafe_allow_html=True)

        with col2:
            links = [create_clickable_link(f"From base {self.start_params} to base {i}", f"{self.start_params}-to-{i}") for i in range(2,17) if self.start_params != i]
            st.markdown("<br>".join(links), unsafe_allow_html=True)

        with col3:
            link1 = [create_clickable_link(f"From base {2} to base {i}", f"{2}-to-{i}") for i in [2,4,8,10,16] if 2 != i]
            link2 = [create_clickable_link(f"From base {i} to base {2}", f"{i}-to-{2}") for i in [2,4,8,10,16] if 2 != i]
            link3 = [create_clickable_link(f"From base {10} to base {i}", f"{10}-to-{i}") for i in [4,8,10,16] if 10 != i]

            st.markdown("<br>".join(link1), unsafe_allow_html=True)
            st.markdown("<br>".join(link2), unsafe_allow_html=True)
            st.markdown("<br>".join(link3), unsafe_allow_html=True)

    # update self.start_params and self.last_params
    def updateParams(self, params = None):
        params = st.query_params
        if params:
            # ดึงข้อมูลจากพารามมาเช็คว่า index แรกทั้งข้างหน้าและข้างหลัง มี "-" ไหม ถ้ามีให้ get แค่ index แรกหน้าหลัง ถ้าไม่ get index สองตัวแรกหน้าหลัง
            self.start_params = int(params.get("convert_from")[0] if params.get("convert_from")[1] == "-" else params.get("convert_from")[0:2])
            # second
            self.last_params = int(params.get("convert_from")[-1] if params.get("convert_from")[-2] == "-" else params.get("convert_from")[-2:])
        else: 
            # default = 2
            self.start_params = 2
            self.last_params = 10
        
    def inputBase(self):
        # create session state to keep swap and count value
        def swapFunc(swap_btn, convert_btn):
            if "swap" not in st.session_state:
                st.session_state.swap = True
            if "count" not in st.session_state:
                st.session_state.count = 2

            if swap_btn:
                # add count to modurate change True, False value in session state
                st.session_state["count"] += 1

            # นำ state count มามอด 2 เพื่อสลับค่า true, false
            if st.session_state.count % 2 == 0:
                st.session_state.swap = True
            elif st.session_state.count % 2 != 0: 
                st.session_state.swap = False

            col1 ,col2 = st.columns(2)

            # condition if True, False swap component
            if st.session_state.swap == True:
                with col1:
                    from_base = st.number_input("From base :", min_value=2, max_value=16, format="%d", value=self.start_params)
                with col2:
                    to_base = st.number_input("From base:", min_value=2, max_value=16, format="%d", value=self.last_params)
                if convert_btn:
                    self.converter(number, from_base, to_base, btn_onclick=convert_btn)
                    
            elif st.session_state.swap == False: 
                with col1:
                    to_base = st.number_input("From base:", min_value=2, max_value=16, format="%d", value=self.last_params)
                with col2:
                    from_base = st.number_input("From base :", min_value=2, max_value=16, format="%d", value=self.start_params)
                if convert_btn:
                    self.converter(number, to_base, from_base, btn_onclick=convert_btn)
        
        st.title("Base Converter")
        number = st.text_input("Enter the number to convert:", value="")

        convert, swap = st.columns(2)
        with convert:
            convert_btn = st.button("Convert!")
        with swap:
            swap_btn = st.button("Swap Base")
        

        swapFunc(swap_btn, convert_btn)
