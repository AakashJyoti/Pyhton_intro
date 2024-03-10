import json


def load_data():
    try:
        with open("Database.txt", "r") as file:
             return json.load(file)
    except FileNotFoundError:
        return []


def save_data(videos):
    with open("Database.txt", "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n Your videos list:")
    if len(videos)== 0 :
        print("--- List is Empty ---")
        return
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video["name"]}, Duration: {video["time"]}")


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to update: "))
    if 1 <=index <=len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[index-1] = {"name": name, "time": time }
        save_data(videos)
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to delete: "))
    if 1 <=index <=len(videos):
        del videos[index-1] 
        save_data(videos)
    else:
        print("Invalid index selected")


def main():
    videos = load_data()
    while True:
        print("\n Video Manager")
        print("Choose an option..")
        print("1. List all video")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")
        choice = input("Enter a choose: ")


        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
