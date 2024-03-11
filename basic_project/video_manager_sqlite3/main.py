import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
"""
)


def list_videos():
    print("Current videos list: ")
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()


def update_video(video_id, name, time):
    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id)
    )
    conn.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()


def main():
    while True:
        print("\n Video manager with DB")
        print("1. List of Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        user_input = input("Enter your choice: ")
        if user_input == "1":
            list_videos()
        elif user_input == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif user_input == "3":
            list_videos()
            video_id = input("Enter video ID to update: ")
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(video_id, name, time)
        elif user_input == "4":
            list_videos()
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif user_input == "5":
            break
        else:
            print("Invalid choice. Please try again")

    conn.close()


if __name__ == "__main__":
    main()
