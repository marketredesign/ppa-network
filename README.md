# ppa-network




# Calculations

**Variables:**

- $P(t)$: Price charged per parcel at time $t$.
- $D(t)$: Demand (number of parcels) at time $t$, calculated using the demand function.
- $C(t)$: Total cost at time $t$, including fixed and variable costs.
- $N(t)$: Number of active network components (e.g., warehouses, routes) at time $t$.
- $F$: Fixed cost associated with operating one network component for a unit of time.
- $V$: Variable cost incurred per parcel handled.
- $a$: Maximum potential demand when the price is zero; represents the intercept of the demand function (total market volume).
- $b$: Demand sensitivity to price; indicates how much demand decreases with a unit increase in price.
- $K$: Capacity limit per network component; maximum number of parcels a component can handle in a given time period.
- $\Pi$: Total profit over the time period $T$.
- $T$: The time horizon over which the optimization is performed.

**Assumptions:**

1. **Demand Function:**

   $D(t) = a - bP(t)$

   - **\( a \)**: Represents the highest possible demand when the price is zero.
   - **\( b \)**: Indicates how much demand decreases as price increases; it reflects the price elasticity of demand.

2. **Cost Function:**

   $C(t) = N(t) \times F + V \times D(t)$

   - $N(t) \times F$: Total fixed costs at time $t$, based on the number of active components.
   - $V \times D(t)$: Total variable costs at time $t$, dependent on the number of parcels handled.

3. **Capacity of Each Network Component:**

   - Each component has a capacity limit $K$, representing the maximum number of parcels it can handle per unit of time (e.g., per day).

**Objective Function:**

- Profit $\Pi$:

  $\Pi = \int_{T} [P(t) \times D(t) - C(t)] \, dt$

  Where $T$ is the time period over which we are optimizing.

**Constraints:**

1. **Demand Allocation Constraint:**

   $D(t) \leq N(t) \times K$

   - Ensures that total demand does not exceed the total capacity provided by the active network components.

2. **Network Component Activation:**

   - $N(t)$ is an integer representing the number of active components and can be adjusted over time.

3. **Non-Negative Variables:**

   - $D(t) \geq 0$
   - $P(t) \geq 0$
   - $N(t) \geq 0$ and integer

**Optimization Problem:**

- Maximize $\Pi$ with respect to $P(t)$ and $N(t)$, subject to the constraints.

**Solution Approach:**

1. **Determine Optimal Price $\( P^*(t) \)$:**

   - Use the demand function to relate price and demand.
   - For a given $N(t)$, solve for $P(t)$ that maximizes profit while ensuring $D(t) \leq N(t) \times K$.

2. **Determine Optimal Number of Active Components $\( N^*(t) \)$:**

   - Based on forecasted demand $D(t)$, adjust $N(t)$ to minimize costs while meeting demand.

3. **Iterative Optimization:**

   - Iterate between adjusting $P(t)$ and $N(t)$ to find the combination that maximizes profit.
