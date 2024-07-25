import requests
import pandas as pd
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt

st.sidebar.success('Malware Data')


def fetch_malware_data(date):
    url = "https://mb-api.abuse.ch/api/v1/"
    payload = {
        'query': 'get_taginfo',
        'tag': 'malware',
        'limit': 1000,
        'date': date
    }
    response = requests.post(url, data=payload)
    data = response.json()
    return data


c = st.date_input('Enter a date: ')

with st.expander("See Date selected"):
    st.write(c)

with st.expander("See Data/Information"):
    date_object = datetime.strptime(str(c), '%Y-%m-%d')
    if date_object > datetime.strptime('2023-12-31', '%Y-%m-%d'):
        st.write("No data available!")
    else:
        raw_data = fetch_malware_data(c)
        st.write(raw_data)

        data = raw_data['data']

        # Parsing the data for different selections
        types_per_year = {}
        for item in data:
            malware_type = item['signature']
            first_seen = item['first_seen']
            year = datetime.strptime(first_seen, "%Y-%m-%d %H:%M:%S").year

            if year not in types_per_year:
                types_per_year[year] = {}

            if malware_type not in types_per_year[year]:
                types_per_year[year][malware_type] = 0

            types_per_year[year][malware_type] += 1

        df = pd.DataFrame(types_per_year).fillna(0).astype(int).T

        # Collecting unique malware types
        all_malware_types = list({item['signature'] for item in data})

        selection = st.multiselect('Choose what data you want specifically', [
            'malware types', 'total counts per year',
            'yearly data for each malware type'
        ] + all_malware_types)

        st.write(selection)
        if 'malware types' in selection:
            st.write('Malware Types: ', all_malware_types)
        if 'total counts per year' in selection:
            st.write('Total Counts Per Year: ', df.sum(axis=1).to_dict())
        if 'yearly data for each malware type' in selection:
            st.write(df)

        for malware_type in all_malware_types:
            if malware_type in selection:
                st.write(f'{malware_type}: ', df[malware_type].to_dict())

        st.title('Malware Attack Counts Per Year')
        st.line_chart(df)

        df.plot(kind='bar', stacked=True, figsize=(10, 5))
        plt.xlabel('Year')
        plt.ylabel('Count')
        plt.title('Malware Attack Counts Per Year')
        plt.xticks(rotation=45)
        st.pyplot(plt)

with st.expander("See All Malware Types"):
    if st.button("Show All Malware Types"):
        st.write(raw_data)
