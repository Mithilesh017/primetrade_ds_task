# Web3 Trader Performance & Market Sentiment Analysis

## Objective
This repository contains an exploratory data analysis (EDA) mapping historical trader data from Hyperliquid against the Bitcoin Market Fear & Greed Index to uncover hidden trading patterns and actionable strategy insights.

## Core Insights Discovered
By merging high-frequency execution data with daily sentiment classifications, several hidden patterns in trader performance emerged:

1. **Extreme Greed Drives the Highest Efficiency:** 
   Traders achieved the highest average profit per trade (~$67.89) during periods of "Extreme Greed", likely capitalizing on strong upward momentum and trend-following strategies.
2. **Fear Drives the Highest Volume & Total PnL:** 
   Periods of "Fear" triggered the highest trading activity (~61.8k trades). Despite the negative sentiment, traders generated their highest *total* gross profit ($3.35M) during these periods, exploiting high volatility through active, high-frequency trading.
3. **Derivatives Directional Bias:**
   * **Short Squeezes in Greed:** Liquidations of Isolated Shorts occurred exclusively during "Greed" periods, resulting in massive negative PnL spikes for short sellers fighting the trend.
   * **Profitable Short Closing in Fear:** The action of "Close Short" was incredibly profitable during "Fear" and "Extreme Fear" periods, indicating traders successfully rode the market down and covered at the bottom.

## Strategic Recommendations
Based on the data, the following Web3 trading strategies are recommended:
* **Momentum Trend-Following:** Scale up position sizing and leverage on "Open Long" trades specifically when sentiment transitions into "Extreme Greed".
* **Volatility Scalping:** Increase trading frequency and deploy grid-trading or mean-reversion strategies during "Fear" to capture the massive volume of small price discrepancies.
* **Avoid Counter-Trending:** Strictly limit "Open Short" positions during "Greed" to avoid catastrophic isolated short liquidations.

## Setup & Execution
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure the datasets (`historical_data DS.csv` and `fear_greed_index DS.csv`) are located in the `/data` folder.
4. Run the analysis: `python eda_analysis.py`

*Note: Visualizations are automatically saved to the `/plots` directory upon execution.*# Web3 Trader Performance & Market Sentiment Analysis

## Objective
This repository contains an exploratory data analysis (EDA) mapping historical trader data from Hyperliquid against the Bitcoin Market Fear & Greed Index to uncover hidden trading patterns and actionable strategy insights.

## Core Insights Discovered
By merging high-frequency execution data with daily sentiment classifications, several hidden patterns in trader performance emerged:

1. **Extreme Greed Drives the Highest Efficiency:** 
   Traders achieved the highest average profit per trade (~$67.89) during periods of "Extreme Greed", likely capitalizing on strong upward momentum and trend-following strategies.
2. **Fear Drives the Highest Volume & Total PnL:** 
   Periods of "Fear" triggered the highest trading activity (~61.8k trades). Despite the negative sentiment, traders generated their highest *total* gross profit ($3.35M) during these periods, exploiting high volatility through active, high-frequency trading.
3. **Derivatives Directional Bias:**
   * **Short Squeezes in Greed:** Liquidations of Isolated Shorts occurred exclusively during "Greed" periods, resulting in massive negative PnL spikes for short sellers fighting the trend.
   * **Profitable Short Closing in Fear:** The action of "Close Short" was incredibly profitable during "Fear" and "Extreme Fear" periods, indicating traders successfully rode the market down and covered at the bottom.

## Strategic Recommendations
Based on the data, the following Web3 trading strategies are recommended:
* **Momentum Trend-Following:** Scale up position sizing and leverage on "Open Long" trades specifically when sentiment transitions into "Extreme Greed".
* **Volatility Scalping:** Increase trading frequency and deploy grid-trading or mean-reversion strategies during "Fear" to capture the massive volume of small price discrepancies.
* **Avoid Counter-Trending:** Strictly limit "Open Short" positions during "Greed" to avoid catastrophic isolated short liquidations.

## Setup & Execution
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure the datasets (`historical_data DS.csv` and `fear_greed_index DS.csv`) are located in the `/data` folder.
4. Run the analysis: `python eda_analysis.py`

*Note: Visualizations are automatically saved to the `/plots` directory upon execution.*