import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_and_merge_data():
    """Loads the CSV files and merges them on the date."""
    print("Loading datasets...")
    # Adjust paths if running outside the root directory
    df_fg = pd.read_csv('data/fear_greed_index DS.csv')
    df_hd = pd.read_csv('data/historical_data DS.csv')

    print("Processing dates and merging...")
    # Convert Hyperliquid Timestamp to Date
    df_hd['Date_IST'] = pd.to_datetime(df_hd['Timestamp IST'], format='%d-%m-%Y %H:%M')
    df_hd['date'] = df_hd['Date_IST'].dt.strftime('%Y-%m-%d')
    
    # Merge on the date string
    merged_df = pd.merge(df_hd, df_fg, on='date', how='left')
    
    # Drop rows where sentiment data is missing
    merged_df = merged_df.dropna(subset=['classification'])
    return merged_df

def analyze_sentiment_pnl(df):
    """Analyzes the relationship between Market Sentiment and Trader PnL."""
    print("\n--- PnL by Market Sentiment ---")
    
    # Group by classification
    sentiment_stats = df.groupby('classification').agg(
        Total_Trades=('Closed PnL', 'count'),
        Total_PnL=('Closed PnL', 'sum'),
        Average_PnL=('Closed PnL', 'mean')
    ).reset_index()
    
    # Sort logically from Extreme Fear to Extreme Greed
    order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
    sentiment_stats['classification'] = pd.Categorical(sentiment_stats['classification'], categories=order, ordered=True)
    sentiment_stats = sentiment_stats.sort_values('classification')
    
    print(sentiment_stats.to_string(index=False))
    return sentiment_stats

def analyze_trade_direction(df):
    """Analyzes profitability of specific derivative actions (Long/Short) based on sentiment."""
    print("\n--- Average PnL by Derivative Direction & Sentiment ---")
    
    # Filter out 0 PnL actions (like Open Long/Short which don't realize PnL immediately)
    realized_df = df[df['Closed PnL'] != 0]
    
    direction_stats = realized_df.groupby(['classification', 'Direction'])['Closed PnL'].mean().unstack()
    print(direction_stats)

def plot_insights(df):
    """Generates visual reports of the data."""
    print("\nGenerating visualizations...")
    os.makedirs('plots', exist_ok=True)
    
    plt.figure(figsize=(12, 6))
    order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
    
    # Plot Average PnL
    sns.barplot(data=df, x='classification', y='Closed PnL', estimator='mean', order=order, errorbar=None, palette='coolwarm')
    plt.title('Average Realized PnL per Trade by Sentiment')
    plt.ylabel('Average PnL (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('plots/avg_pnl_by_sentiment.png')
    print("Saved plot to plots/avg_pnl_by_sentiment.png")

if __name__ == "__main__":
    merged_data = load_and_merge_data()
    analyze_sentiment_pnl(merged_data)
    analyze_trade_direction(merged_data)
    plot_insights(merged_data)
    print("\nAnalysis Complete.")