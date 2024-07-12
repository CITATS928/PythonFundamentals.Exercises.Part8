import os

# tree.py at the bottom would be:

def walk(dirname, file_handler):
    #if it's file, print it out, if not call walk()
    for item in os.listdir(dirname):
        item_path = os.path.join(dirname, item)
        # 如果是文件，写入文件
        if os.path.isfile(item_path):
            file_handler.write(f"{item_path}\n")
        # 如果是目录，递归调用 walk 函数
        elif os.path.isdir(item_path):
            file_handler.write(f"{item_path}/\n")
            walk(item_path, file_handler)

if __name__ == '__main__':
    with open("exercise_2.txt", "w") as file_handler:
        walk(".", file_handler)