import json
from datetime import datetime

DATA_FILE = "schedule.json"

def load_schedule():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_schedule(schedule):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(schedule, file, indent=4)

def add_event(schedule, title, date, time, description):
    event = {
        "title": title,
        "date": date,
        "time": time,
        "description": description
    }
    schedule.append(event)
    print(f"事件“{title}”已添加！")

def view_schedule(schedule):
    if schedule:
        print("\n所有日程事件：")
        for idx, event in enumerate(sorted(schedule, key=lambda x: (x["date"], x["time"])), 1):
            print(f"{idx}. {event['title']} | 日期：{event['date']} | 时间：{event['time']} | 描述：{event['description']}")
    else:
        print("没有任何日程事件。")

def delete_event(schedule, index):
    if 0 <= index < len(schedule):
        deleted_event = schedule.pop(index)
        print(f"事件“{deleted_event['title']}”已删除。")
        save_schedule(schedule)
    else:
        print("无效的事件索引。")

def view_upcoming_events(schedule):
    now = datetime.now()
    upcoming_events = [event for event in schedule if datetime.strptime(event['date'] + " " + event['time'], "%Y-%m-%d %H:%M") > now]
    
    if upcoming_events:
        print("\n即将到来的事件：")
        for idx, event in enumerate(sorted(upcoming_events, key=lambda x: (x["date"], x["time"])), 1):
            print(f"{idx}. {event['title']} | 日期：{event['date']} | 时间：{event['time']} | 描述：{event['description']}")
    else:
        print("没有即将到来的事件。")

if __name__ == "__main__":
    schedule = load_schedule()
    print("欢迎使用个人日程管理系统！")

    while True:
        print("\n请选择一个操作：")
        print("1. 添加新事件")
        print("2. 查看所有事件")
        print("3. 删除事件")
        print("4. 查看即将到来的事件")
        print("5. 退出")

        choice = input("请输入选项（1/2/3/4/5）：")

        if choice == "1":
            title = input("请输入事件标题：")
            date = input("请输入事件日期（格式YYYY-MM-DD）：")
            time = input("请输入事件时间（格式HH:MM）：")
            description = input("请输入事件描述：")
            add_event(schedule, title, date, time, description)
            save_schedule(schedule)
        elif choice == "2":
            view_schedule(schedule)
        elif choice == "3":
            index = int(input("请输入要删除的事件编号：")) - 1
            delete_event(schedule, index)
            save_schedule(schedule)
        elif choice == "4":
            view_upcoming_events(schedule)
        elif choice == "5":
            print("感谢使用个人日程管理系统，再见！")
            break
        else:
            print("无效选项，请重新选择。")
