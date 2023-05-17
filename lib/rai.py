
import streamlit as st

from railib import api
from railib.credentials import ClientCredentials

ctx = api.Context(
   region=st.secrets["rai"]["region"],
   host=st.secrets["rai"]["host"],
   port=st.secrets["rai"]["port"],
   credentials=ClientCredentials(
     st.secrets["rai"]["client_id"],
     st.secrets["rai"]["client_secret"],
     st.secrets["rai"]["client_credentials_url"]
   ),
   audience=st.secrets["rai"]["audience"]
)

def rai_query(query: str, readonly: bool = True):
    rsp = api.exec(
        ctx,
        database=st.secrets["rai"]["database"],
        engine=st.secrets["rai"]["engine"],
        command=query,
        readonly=readonly,
    )
    dfs = [
        relation["table"].to_pandas() for relation in rsp.results
    ]
    return dfs