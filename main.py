import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_netflix():
    try:
        # Load Netflix dataset
        netflix_df = pd.read_csv('netflix_titles.csv')
        
        # Content type analysis
        plt.figure(figsize=(10, 6))
        sns.countplot(data=netflix_df, x='type')
        plt.title('Count of Movies vs TV Shows')
        plt.xlabel('Content Type')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.savefig('netflix_content_types.png')
        plt.close()
        
        # Genre analysis
        genres = netflix_df['listed_in'].str.split(',', expand=True).stack()
        plt.figure(figsize=(12, 6))
        sns.countplot(y=genres, order=genres.value_counts().head(10).index)
        plt.title('Top 10 Netflix Genres')
        plt.xlabel('Count')
        plt.ylabel('Genre')
        plt.tight_layout()
        plt.savefig('netflix_genres.png')
        plt.close()
        
        # Release year analysis
        plt.figure(figsize=(12, 6))
        sns.histplot(data=netflix_df, x='release_year', bins=30)
        plt.title('Netflix Content Released by Year')
        plt.xlabel('Release Year')
        plt.ylabel('Number of Titles')
        plt.tight_layout()
        plt.savefig('netflix_yearly_releases.png')
        plt.close()
        
        # Print some statistics
        print('\nNetflix Analysis Results:')
        print('\nTotal content:', len(netflix_df))
        print('\nContent Type Distribution:')
        print(netflix_df['type'].value_counts())
        print('\nTop 10 Genres:')
        print(genres.value_counts().head(10))
        
    except FileNotFoundError:
        print("\nError: Netflix dataset not found!")
        print("Please ensure 'netflix_titles.csv' is in the current directory.")

def analyze_playstore():
    try:
        # Load Play Store dataset
        playstore_df = pd.read_csv('googleplaystore.csv')
        
        # Category analysis
        plt.figure(figsize=(12, 6))
        sns.countplot(data=playstore_df, y='Category', order=playstore_df['Category'].value_counts().index)
        plt.title('Most Popular App Categories')
        plt.xlabel('Number of Apps')
        plt.tight_layout()
        plt.savefig('playstore_categories.png')
        plt.close()
        
        # Rating distribution
        plt.figure(figsize=(10, 6))
        sns.histplot(data=playstore_df, x='Rating', bins=50)
        plt.title('Distribution of App Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.savefig('playstore_ratings.png')
        plt.close()
        
        # Free vs Paid analysis
        plt.figure(figsize=(8, 6))
        sns.boxplot(data=playstore_df, x='Type', y='Rating')
        plt.title('Rating Distribution: Free vs Paid Apps')
        plt.xlabel('App Type')
        plt.ylabel('Rating')
        plt.tight_layout()
        plt.savefig('playstore_free_vs_paid.png')
        plt.close()
        
        # Print some statistics
        print('\nGoogle Play Store Analysis Results:')
        print('\nTotal number of apps:', len(playstore_df))
        print('\nTop 5 Categories:')
        print(playstore_df['Category'].value_counts().head())
        print('\nAverage Ratings by Type:')
        print(playstore_df.groupby('Type')['Rating'].mean())
        
    except FileNotFoundError:
        print("\nError: Google Play Store dataset not found!")
        print("Please download 'googleplaystore.csv' from Kaggle and place it in the current directory:")
        print("https://www.kaggle.com/datasets/lava18/google-play-store-apps")

def main():
    print("Starting Netflix content analysis...")
    analyze_netflix()
    print("\nStarting Google Play Store analysis...")
    analyze_playstore()
    print("\nAnalysis complete! Check the generated PNG files for visualizations.")

if __name__ == '__main__':
    main()