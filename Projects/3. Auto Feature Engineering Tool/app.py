import streamlit as st
from helpers import *

def main():
    st.title('Auto Feature Selector Tool')

    #File uploader
    upload_file = st.file_uploader('Choose a csv file',type='csv')
    if upload_file is not None:
        analyze_csv_file(upload_file)




 





if __name__ == '__main__':
    main()
