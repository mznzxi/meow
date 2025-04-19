import matplotlib.pyplot as plt
import numpy as np

# Set up figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# ---- Left plot: Market Supply and Demand ----
# Quantity range
Q_market = np.linspace(0, 100, 100)

# Demand and Supply curves
P_demand = 100 - 0.5 * Q_market
P_supply = 20 + 0.5 * Q_market

# Plot market supply and demand
ax1.plot(Q_market, P_demand, label='수요곡선 (Demand)', color='blue')
ax1.plot(Q_market, P_supply, label='공급곡선 (Supply)', color='red')
ax1.set_title("시장 전체의 수요와 공급")
ax1.set_xlabel("시장 수량 (Q)")
ax1.set_ylabel("가격 (P)")
ax1.legend()
ax1.grid(True)

# Find market equilibrium
eq_quantity = 80
eq_price = 60
ax1.plot(eq_quantity, eq_price, 'ko')  # Equilibrium point
ax1.annotate(f"시장균형 (P={eq_price}, Q={eq_quantity})", 
             xy=(eq_quantity, eq_price), xytext=(50, 80),
             arrowprops=dict(arrowstyle="->"))

# ---- Right plot: Individual firm's horizontal demand curve ----
Q_firm = np.linspace(0, 100, 100)
P_firm = np.full_like(Q_firm, eq_price)

# Plot firm's demand curve
ax2.plot(Q_firm, P_firm, label='기업의 수요곡선 (D = MR = P)', color='green')
ax2.set_title("개별 기업의 수요곡선")
ax2.set_xlabel("기업의 산출량 (q)")
ax2.set_ylabel("가격 (P)")
ax2.set_ylim(0, 100)
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()
