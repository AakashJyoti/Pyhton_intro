from pymongo import MongoClient
from bson import ObjectId


client = MongoClient(
    "mongodb+srv://Aakash_mongo:GdsGoPluG4Yd4CzL@cluster0.1zyyhly.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

DB = client["vidmanager"]
video_collection = DB["video"]

# print(video_collection)


def list_videos():
    for video in video_collection.find():
        print(f"ID: {video["_id"]}, Video: {video["name"]}, Duration: {video["time"]}")


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


def update_video(video_id, name, time):
    video_collection.update_one({"_id": ObjectId(video_id)}, {"$set": {"name": name, "time": time}})


def delete_video(video_id):
    video_collection.find_one_and_delete(video_id)


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


if __name__ == "__main__":
    main()
