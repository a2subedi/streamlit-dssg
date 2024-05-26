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

from typing import Any

import numpy as np
import matplotlib.pyplot as plt

import streamlit as st
from streamlit.hello.utils import show_code
from constants import PATHS

import pandas as pd
from prophet import Prophet


def animation_demo() -> None:

    # DATASET
    df_raw = pd.read_csv(PATHS["DATASET"])
    # st.write(df.head())

    # METADATA COUNTRIES
    df_cou = pd.read_csv(PATHS["METADATA_COUNTRIES"])
    # st.write(df_cou.head())

    # METADATA_INDICATORS
    df_ind = pd.read_csv(PATHS["METADATA_INDICATORS"])
    # st.write(df_ind.head())
    
    df_map = pd.read_csv(PATHS['METADATA_MAPPINGS'])
    df_map_filtered = df_map[df_map["Use Case 3"] == 3]
    # st.write(df_map_filtered.head())

    # Prepare selection list for indicator and countries/regions
   
    indicator_choice = st.multiselect(
        "Choose Indicator(s)", list(df_map_filtered["Dataset"]), None
    )
    indicator_choice_detail = df_ind[df_ind["INDICATOR_NAME"].isin(indicator_choice)]
    
    
    countries = st.multiselect(
        "Choose countries/region", list(df_cou["TableName"]), None
    )
    
    if not indicator_choice:
        st.error("Please select at least one indicator.")
    if not countries:
        st.error("Please select at least one country.")
    else:
        for indicator in indicator_choice:
            df = df_raw.copy()
            filtered_df = df[
                (df["Indicator Name"]==indicator) & (df["Country Name"].isin(countries))
            ]
            filtered_df.dropna()
            
            df_pivot = filtered_df[(filtered_df["Indicator Name"]== indicator) & filtered_df["Country Name"].isin(countries)]\
                    .pivot(index="year", columns="Country Name", values="value")

            df = pd.DataFrame(df_pivot).T
            if indicator_choice and countries:
                st.write(indicator + ' Over the years :')
            st.line_chart(df.T)
            
        
    
st.set_page_config(page_title="Explore Dataset", page_icon="📹")
st.markdown("# Explore Dataset")
st.sidebar.header("Explore Dataset")
st.write(
    """Choose different Country code/ Region code and indicators to explore dataset"""
)

animation_demo()

# show_code(animation_demo)
