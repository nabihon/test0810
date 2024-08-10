import streamlit as st
import pandas as pd
import altair as alt

# 샘플 데이터 생성
@st.cache
def load_data():
    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value1': [100, 150, 200, 250, 300],
        'Value2': [120, 180, 240, 300, 360],
        'Value3': [90, 130, 170, 210, 250]
    })
    return data

data = load_data()

# 대시보드 제목
st.title("Simple Data Analysis Dashboard")

# 데이터 테이블 표시
st.header("Dataset")
st.write(data)

# 필터 설정
st.sidebar.header("Filter Options")
category = st.sidebar.selectbox("Select Category", data['Category'].unique())

# 선택된 카테고리 데이터 필터링
filtered_data = data[data['Category'] == category]

# 필터된 데이터 표시
st.subheader(f"Data for Category: {category}")
st.write(filtered_data)

# 데이터 시각화
st.header("Data Visualization")

# Altair를 이용한 막대 차트
bar_chart = alt.Chart(filtered_data).mark_bar().encode(
    x='Category:N',
    y='Value1:Q',
    color='Category:N'
).properties(
    title="Bar Chart of Value1"
)

line_chart = alt.Chart(filtered_data).mark_line().encode(
    x='Category:N',
    y='Value2:Q',
    color='Category:N'
).properties(
    title="Line Chart of Value2"
)

st.altair_chart(bar_chart, use_container_width=True)
st.altair_chart(line_chart, use_container_width=True)

# 결론 또는 요약 표시
st.header("Summary")
st.write("This dashboard provides a basic analysis of the dataset.")