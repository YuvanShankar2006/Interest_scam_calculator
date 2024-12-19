import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Financial Calculator", page_icon="", layout="wide")

# Custom CSS to make it more attractive
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .sidebar .sidebar-content {
        background: #ffffff
    }
    h1 {
        color: #1E3A8A;
    }
</style>
""", unsafe_allow_html=True)

st.title(" Financial Calculator")

# Sidebar for inputs
st.sidebar.header("Input Parameters")

p = st.sidebar.number_input("Enter the amount", min_value=0, value=1000, step=100, help="Enter the initial amount")
v = st.sidebar.number_input("Enter the return for each month", min_value=0, value=100, step=10, help="Enter the monthly return")
r = st.sidebar.number_input("Enter the rate of interest (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.1, help="Enter the interest rate")
m = st.sidebar.number_input("Enter the number of Months", min_value=1, value=12, step=1, help="Enter the number of months")

if st.sidebar.button("Calculate"):
    t = p
    k = v
    tot = 0
    data = []

    for i in range(m):
        interest = (p * r) / 100
        tot += interest
        pb = v - interest
        p = p - pb
        data.append({"Month": i + 1, "Interest": round(interest, 2), "Principal Return": round(pb, 2), "Remaining Principal": round(p, 2)})

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Display results
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Monthly Breakdown")
        st.dataframe(df)

    with col2:
        st.subheader("Summary")
        st.write(f"Total interest: {round(tot, 2)}")
        acm = (t + tot) / m
        st.write(f"Actual EMI: {round(acm, 2)}")
        loss = k - acm
        st.write(f"You are having a {'loss' if loss > 0 else 'gain'} of rupees: {round(abs(loss), 2)}")
        total_loss = (k - acm) * m
        st.write(f"Total loss: {round(total_loss, 2)}")

    # Visualizations
    st.subheader("Visualizations")

    # Line chart for Principal and Interest over time
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Month'], y=df['Remaining Principal'], mode='lines+markers', name='Remaining Principal'))
    fig.add_trace(go.Scatter(x=df['Month'], y=df['Interest'], mode='lines+markers', name='Interest'))
    fig.update_layout(title='Principal and Interest Over Time', xaxis_title='Month', yaxis_title='Amount')
    st.plotly_chart(fig)

    # Pie chart for Total Interest vs Principal
    labels = ['Total Interest', 'Principal']
    values = [tot, t]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_layout(title='Total Interest vs Principal')
    st.plotly_chart(fig)

else:
    st.info("Please enter the parameters and click 'Calculate' to see the results.")
