import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Parcel Logistics Pricing and Network Optimization")

    st.sidebar.header("Input Parameters")

    # Input parameters
    a = st.sidebar.number_input("Maximum Potential Demand (a)", value=5000, step=100)
    b = st.sidebar.number_input("Demand Sensitivity to Price (b)", value=200, step=10)
    F = st.sidebar.number_input("Fixed Cost per Network Component (F) in €", value=1000, step=100)
    V = st.sidebar.number_input("Variable Cost per Parcel (V) in €", value=5, step=1)
    K = st.sidebar.number_input("Capacity per Network Component (K)", value=1000, step=100)
    price_range = st.sidebar.slider("Price Range (€)", min_value=1, max_value=50, value=(1, 50), step=1)

    # Generate price points
    P = np.linspace(price_range[0], price_range[1], 500)
    D = a - b * P  # Demand function
    D = np.maximum(D, 0)  # Ensure demand is not negative

    # Calculate number of network components needed
    N = np.ceil(D / K)

    # Calculate total cost
    C = N * F + V * D

    # Calculate revenue
    Revenue = P * D

    # Calculate profit
    Profit = Revenue - C

    # Find optimal price (maximum profit)
    max_profit_index = np.argmax(Profit)
    optimal_price = P[max_profit_index]
    optimal_demand = D[max_profit_index]
    optimal_N = N[max_profit_index]
    optimal_profit = Profit[max_profit_index]

    # Display optimal values
    st.header("Optimal Values")
    st.write(f"**Optimal Price (P\*)**: €{optimal_price:.2f}")
    st.write(f"**Optimal Demand (D(P\*))**: {int(optimal_demand)} parcels")
    st.write(f"**Optimal Number of Network Components (N\*)**: {int(optimal_N)}")
    st.write(f"**Maximum Profit (Π)**: €{optimal_profit:.2f}")

    # Plotting
    st.header("Profit vs. Price")
    fig, ax = plt.subplots()
    ax.plot(P, Profit, label='Profit (Π)')
    ax.axvline(optimal_price, color='r', linestyle='--', label=f'Optimal Price (€{optimal_price:.2f})')
    ax.set_xlabel('Price (€)')
    ax.set_ylabel('Profit (€)')
    ax.set_title('Profit as a Function of Price')
    ax.legend()
    st.pyplot(fig)

    st.header("Demand and Number of Network Components vs. Price")
    fig2, ax2 = plt.subplots()
    ax2.plot(P, D, label='Demand D(P)', color='g')
    ax2.set_xlabel('Price (€)')
    ax2.set_ylabel('Demand (parcels)', color='g')
    ax2.tick_params(axis='y', labelcolor='g')

    ax3 = ax2.twinx()
    ax3.plot(P, N, label='Number of Network Components N', color='b')
    ax3.set_ylabel('Number of Network Components', color='b')
    ax3.tick_params(axis='y', labelcolor='b')

    fig2.tight_layout()
    st.pyplot(fig2)

    # Show data table if checkbox is selected
    if st.checkbox("Show Data Table"):
        data = pd.DataFrame({
            'Price (€)': P,
            'Demand (parcels)': D,
            'Number of Components': N,
            'Total Cost (€)': C,
            'Revenue (€)': Revenue,
            'Profit (€)': Profit
        })
        st.dataframe(data)

if __name__ == '__main__':
    main()
