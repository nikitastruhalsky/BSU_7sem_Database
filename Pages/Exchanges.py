import streamlit as st
import pandas as pd
from sqlalchemy import text, create_engine


name = 'DS_lab2'
user = 'postgres'
password = '1234'
port = 9248
engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@localhost:{port}/{name}"
)
exchanges = pd.read_sql_query(f"SELECT * FROM exchanges", con=engine)


df = pd.read_sql_query(f"SELECT * FROM exchanges", con=engine)
df = df.set_index(df.columns[0], drop=True)
pd_dict = {}
for col, dtype in df.dtypes.items():
    pd_dict[col] = pd.Series([], dtype=dtype)
add_df = pd.DataFrame(pd_dict)
edited = st.data_editor(df[~df["delete"]].copy(), hide_index=True,
        column_config={
            "exchange_size": st.column_config.SelectboxColumn("Exchange size", options=list(range(1, 4)), required=True)
        }
    )
if st.button("Edit data"):
    id_col = df.index.name
    with engine.begin() as conn:
        edited_rows = edited[(df[~df["delete"]] != edited).sum(axis=1) > 0]
        if len(edited_rows) > 0:
            edited_rows.to_sql('temp_table', engine, if_exists='replace')
            for col in edited_rows.columns:
                sql = f"UPDATE exchanges AS f SET {col} = t.{col} FROM temp_table AS t WHERE f.{id_col} = t.{id_col}"
                conn.execute(text(sql))

added = st.data_editor(add_df, hide_index=True, num_rows="dynamic",
    column_config={
        "exchange_size": st.column_config.SelectboxColumn("Exchange size", options=list(range(1, 4)), required=True),
        "delete": None,
    }
)
if st.button("Add data"):
    last_ind = max(df.index) + 1
    added.index = list(range(last_ind, last_ind + len(added)))
    added["delete"] = False
    if len(added) > 0:
        with engine.begin() as conn:
            added.to_sql('temp_table', engine, if_exists='replace')
            sql = f"INSERT INTO exchanges (SELECT * FROM temp_table)"
            conn.execute(text(sql))
            add_df = None
    st.write("Done")
