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

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="DSSG Datathon",
        page_icon="👋",
    )

    st.write("# About the project! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        ### Predicting Economic Growth through Educational Attainment. 
        **Main Goal:** Analyze the impact of educational attainment on economic growth and development.  
        
        **Main Challenge:** Investigate the correlation between education metrics, e.g. literacy rates, school enrollment rates, educational expenditures etc., and economic indicators, e.g., GDP growth, employment rates etc. Develop models to predict how improvements in education could drive economic growth in different regions.  
        
        **Data Source:** [World Bank Indicators](https://data.worldbank.org/indicator?tab=featured)


        **Collaborators**
        - [Abhishek Subedi](https://github.com/a2subedi)
        - [Ishan Lamsal](https://github.com/ishanism) 

        
        -*Customized using templete [streamlit-hello repo](https://github.com/streamlit/streamlit-hello)*


    """
    )


if __name__ == "__main__":
    run()
