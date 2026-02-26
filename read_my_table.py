# read_movies.py
# Reads all items from the DynamoDB Movies table and prints them.
# Part of Lab 09 — feature/read-dynamo branch

import boto3
from boto3.dynamodb.conditions import Key

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Playlist"


def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_movie(playlist):
    """Print a single movie's details in a readable format."""
    title = playlist.get("Title", "Unknown Title")
    artist = playlist.get("Artist", "Unknown Artist")
    rating = playlist.get("Rating", "Unkown Ratings")
    
    # Ratings is a nested map in the table — handle it gracefully
    
    print(f"  Title : {title}")
    print(f"  Artist  : {artist}")
    print(f"  Rating  : {rating}")


def print_all_songs():
    """Scan the entire Movies table and print each item."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No songs found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} movie(s):\n")
    for movie in items:
        print_movie(movie)

def main():
    print("===== Reading from DynamoDB =====\n")
    #print_all_movies()
    print_all_songs()


if __name__ == "__main__":
    main()
