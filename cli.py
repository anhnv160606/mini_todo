import argparse
from todo import TodoList


def main():
    todo_list = TodoList()
    parser = argparse.ArgumentParser(description="Quản lý công việc")
    subparsers = parser.add_subparsers(dest="command")

    # Lệnh 'add'
    add_parser = subparsers.add_parser("add", help="Thêm công việc mới")
    add_parser.add_argument("task_name", type=str, help="Tên công việc")

    # Lệnh 'list'
    subparsers.add_parser("list", help="Hiển thị danh sách công việc")

    args = parser.parse_args()

    if args.command == "add":
        try:
            print(todo_list.add_task(args.task_name))
        except ValueError as e:
            print(f"Lỗi: {e}")
    elif args.command == "list":
        print(todo_list.list_tasks())


if __name__ == "__main__":
    main()