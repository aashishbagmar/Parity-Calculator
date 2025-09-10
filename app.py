import streamlit as st

st.set_page_config(page_title="Oil Miller Parity Calculator", layout="centered")

st.title("🛢️ Oil Miller Parity Calculator")

st.markdown("Enter values to calculate parity and cake cost %.")

# --- Inputs ---
cotton_seed_rate = st.number_input("Cotton Seed Rate (₹/Quintal)", min_value=0.0, value=0.0, step=10.0)
expenses = st.number_input("Expenses (₹/Quintal)", min_value=0.0, value=0.0, step=10.0)
transport  = st.number_input("Transport (₹/Quintal)", min_value=0.0, value=0.0, step=0.1)
oil_rate = st.number_input("Oil Rate (₹/10kg)", min_value=0.0, value=0.0, step=50.0)
oil_outturn_per10kg = st.number_input("Oil %", min_value=0.0, value=0.0, step=0.1)
manufacturing_loss_percent = st.number_input("Manufacturing loss %", min_value=0.0, max_value=100.0, value=80.0, step=0.1)

# --- Calculation ---
if st.button("Calculate"):
    seed_qty_kg = 100  # 1 Quintal = 100 kg

    # Oil produced (kg) from 100kg
    oil_produced_kg = (oil_outturn_per10kg / 100) * seed_qty_kg  

    # Oil revenue per quintal
    oil_revenue = (oil_produced_kg * oil_rate) / 10

    cake_outturn_percent = 100 - oil_outturn_per10kg - manufacturing_loss_percent

    # Cake produced (kg)
    cake_produced_kg = seed_qty_kg * (cake_outturn_percent / 100)  

    # Total cost (seed + expenses)
    total_cost = cotton_seed_rate + expenses  + transport 

    # Remaining cost after oil revenue
    cake_cost_total = total_cost - oil_revenue  

    # Cake cost per kg
    cake_cost_perkg = int(((cake_cost_total / (cake_produced_kg if cake_produced_kg else 1)) * 100) * 1.05) # per 100 kg cake 

    # Cake cost %
    cake_cost_percent = int((cake_cost_perkg / (cake_cost_total / seed_qty_kg)) * 100) if cake_cost_total != 0 else 0

    cost_per_bag = int(cake_cost_perkg * 0.6)


    # --- Results ---
    st.subheader("📊 Results")
    st.write(f"**Cake Cost per Quintal:** ₹ {cake_cost_perkg:,.0f}")
    st.write(f"**Cake Cost per Bag (60kg):** ₹ {cost_per_bag:,.0f}")
    st.write(f"**Cake %:** {cake_outturn_percent:.2f} %")
    st.write(f"**Oil Produced:** {oil_produced_kg:.0f} kg per quintal")
    st.write(f"**Oil Revenue:** ₹ {oil_revenue:,.0f}")
    st.write(f"**Cake Produced:** {cake_produced_kg:.0f} kg per quintal")
    st.write(f"**Total Cost:** ₹ {total_cost:,.0f}")
    st.write(f"**Remaining Cost for Cake:** ₹ {cake_cost_total:,.0f}")
   































