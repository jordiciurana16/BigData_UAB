import pandas as pd
import isodate

df = pd.read_excel("class5/KEXP.xlsx")
columns = df.columns

# Number of rows and columns
num_rows, num_columns = df.shape
print(f'The dataset has {num_rows} rows and {num_columns} columns.')

# Display the columns
print('The columns in the dataset are:')
for column in columns:
    print(f'- {column}')

# Add columns with engagement, absolute deviation, and percentage deviation
df["engagement"] = df["likeCount"] + df["commentCount"]

avg_viewers = df['viewCount'].mean()
avg_comments = df['commentCount'].mean()
avg_likes = df['likeCount'].mean()

df['Absolute Deviation Viewers'] = df['viewCount'] - avg_viewers
df['Percentage Deviation Viewers'] = round(((df['Absolute Deviation Viewers'] / avg_viewers) * 100), 2)

df['Absolute Deviation Comments'] = df['commentCount'] - avg_comments
df['Percentage Deviation Comments'] = round(((df['Absolute Deviation Comments'] / avg_comments) * 100), 2)

df['Absolute Deviation Likes'] = df['likeCount'] - avg_likes
df['Percentage Deviation Likes'] = round(((df['Absolute Deviation Likes'] / avg_likes) * 100), 2)

# Drop unnecessary columns
df = df.drop(["channelId", "categoryId", "channelTitle", "tags", "publishedAt", "blocked_at"], axis=1)

# Most viewed and most commented videos
index_max_viewers = df["viewCount"].idxmax()
most_viewed_video = df.loc[index_max_viewers, "title"]

index_max_comments = df["commentCount"].idxmax()
most_commented_video = df.loc[index_max_comments, "title"]

print(f'The most viewed video is: {most_viewed_video}')
print(f'The most commented video is: {most_commented_video}')

# Save the DataFrame to a new Excel file
df.to_excel("new_dataset.xlsx", index=False)
