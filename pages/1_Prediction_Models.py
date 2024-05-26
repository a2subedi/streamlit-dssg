# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code
from constants import PATHS



def plotting_demo():
    last_rows = np.random.randn(1, 1)
    option = st.selectbox(
        'Please select a model',
        ('Model1', 'Model2', 'Model3'))
    options = st.multiselect(
    "Please select data regions",
    ["USA", "DEU", "AUS", "NPL"]
    )

    st.write("You selected:", options)
    st.write('You selected:', option)
    chart = st.line_chart(last_rows)

    
    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.


st.set_page_config(page_title="Prediction Models", page_icon="📈")
st.markdown("# Prediction Models")
st.sidebar.header("Prediction Models")
st.write(
    """This demo illustrates output of diffrent prediction models"""
)

plotting_demo()

# show_code(plotting_demo)
