import streamlit as st
import plotly.graph_objects as go

def generate_graphs(match_scores):
    labels = list(match_scores.keys())[:-1]  # Exclude Overall Match %
    values = list(match_scores.values())[:-1]

    # Pie Chart
    fig1 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
    st.plotly_chart(fig1, use_container_width=True)

    # Bar Chart
    fig2 = go.Figure(data=[go.Bar(x=labels, y=values)])
    st.plotly_chart(fig2, use_container_width=True)

    # Gauge Chart
    fig3 = go.Figure()
    fig3.add_trace(go.Indicator(
        mode="gauge+number",
        value=match_scores["Overall Match %"],
        title={'text': "Overall Fit %"},
        gauge={"axis": {"range": [0, 100]}}
    ))
    st.plotly_chart(fig3, use_container_width=True)
