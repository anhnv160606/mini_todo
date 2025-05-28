import argparse
from todo import TodoList


def main():
    todo_list = TodoList()
    parser = argparse.ArgumentParser(description="Quản lý công việc")

    # Thêm lệnh 'add'
    subparsers = parser.add_subparsers(dest="command")
    add_parser = subparsers.add_parser("add", help="Thêm công việc mới")
    add_parser.add_argument("task_name", type=str, help="Tên công việc")

    args = parser.parse_args()

    if args.command == "add":
        try:
            result = todo_list.add_task(args.task_name)
            print(result)
        except ValueError as e:
            print(f"Lỗi: {e}")


if __name__ == "__main__":
    main()