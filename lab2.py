from sqlalchemy import create_engine
from sqlalchemy import text
import streamlit as st
import pandas as pd


class exchange_class:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return self.name


st.set_page_config(layout="wide")
name = 'DS_lab2'
user = 'postgres'
password = '1234'
port = 9248
engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@localhost:{port}/{name}"
)

tables = pd.read_sql_query("""SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';""",
                           con=engine)
tables = [t for t in tables["table_name"].tolist() if t != "temp_table"]
table = st.selectbox("Select table", options=tables[::-1])
exchanges = pd.read_sql_query(f"SELECT * FROM exchanges", con=engine)
df = pd.read_sql_query(f"SELECT * FROM {table}", con=engine)
df = df.set_index(df.columns[0], drop=True)
pd_dict = {}
for col, dtype in df.dtypes.items():
    pd_dict[col] = pd.Series([], dtype=dtype)
add_df = pd.DataFrame(pd_dict)
mapper = {id_exchange: name for id_exchange, name in zip(exchanges["exchange_id"].tolist(), exchanges["exchange_name"].tolist())}
if table == "companies":
    temp_df = df[~df["delete"]].copy()
    temp_df["change_exchange"] = False
    temp_df["exchange_name"] = [mapper[x["exchange_id"]] for ind, x in temp_df.iterrows()]
    edited = st.data_editor(
        temp_df,
        hide_index=True,
        column_config={
            "exchange_size": st.column_config.SelectboxColumn("Exchange size", options=list(range(1, 4)), required=True),
            "exchange_id": None,
            "exchange_name" : st.column_config.Column(disabled=True)
        },
    )
else:
    edited = st.data_editor(
        df[~df["delete"]].copy(),
        hide_index=True,
        column_config={
            "exchange_size": st.column_config.SelectboxColumn("Exchange size", options=list(range(1, 4)), required=True),
        },
    )

if st.button("Edit data"):
    id_col = df.index.name
    with engine.begin() as conn:
        if table != "exchanges": edited = edited.drop(["change_exchange", "exchange_name"], axis=1)
        edited_rows = edited[(df[~df["delete"]] != edited).sum(axis=1) > 0]
        if len(edited_rows) > 0:
            edited_rows.to_sql('temp_table', engine, if_exists='replace')
            for col in edited_rows.columns:
                sql = f"UPDATE {table} AS f SET {col} = t.{col} FROM temp_table AS t WHERE f.{id_col} = t.{id_col}"
                conn.execute(text(sql))
else:
    if table == "companies":
        exchanges = pd.read_sql_query(f"SELECT * FROM exchanges", con=engine)
        exchanges = [exchange_class(x["exchange_name"], x["exchange_id"]) for ind, x in exchanges.iterrows()]
        change_df = edited[edited["change_exchange"]]
        with st.form("form"):
            st.write("Edit exchange for chosen entry")
            label_select = "No entry selected" if len(change_df) == 0 else change_df.iloc[0, :]["company_name"]
            new_user = st.selectbox(options=exchanges, label=label_select)
            b = st.form_submit_button("change")
            if b:
                with engine.begin() as conn:
                    sql = f"UPDATE {table} AS f SET exchange_id = {new_user.id} WHERE company_id = {change_df.index[0]}"
                    conn.execute(text(sql))
added = st.data_editor(
    add_df, hide_index=True, num_rows="dynamic",
    column_config={
        "exchange_size": st.column_config.SelectboxColumn("Exchange size", options=list(range(1, 4)), required=True),
        "delete": None,
    },
)
if st.button("Add data"):
    last_ind = max(df.index) + 1
    added.index = list(range(last_ind, last_ind + len(added)))
    added["delete"] = False
    if len(added) > 0:
        with engine.begin() as conn:
            added.to_sql('temp_table', engine, if_exists='replace')
            sql = f"INSERT INTO {table} (SELECT * FROM temp_table)"
            conn.execute(text(sql))
            add_df = None
    st.write("Done")
