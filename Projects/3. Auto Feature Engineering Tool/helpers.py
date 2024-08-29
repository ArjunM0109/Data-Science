import numpy as np
import pandas as pd
import streamlit as st


def analyze_csv_file(file):
    df = pd.read_csv(file)
    df = st.session_state.get('df',df)
    st.write(df)

    if 'columns_removed' not in st.session_state:
        st.write(f'**columns:** {list(df.columns)}')

        selected_columns=st.multiselect('Selectcolumns to remove',options=df.columns)
        if st.button('Remove Selected Columns'):
            if selected_columns:
                df = df.drop(columns=selected_columns)
                st.session_state['df'] = df
                st.session_state['columns_removed'] = True
                st.success(f'Columns Removed:{','.join(selected_columns)}')
                st.write('### DataFrame After Removing Selected Columns')
                st.write(df)