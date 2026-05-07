import os

from my_01_study.utils.root_utils import root_path

FILE_PATH = f"{root_path}/sais/data_16/old_data"  # ...

def main():
    print("=" * 60)
    print("  ...")
    print("=" * 60)
    # /home/develop_workspaces/study_03/my_302_Protenix  # 工作目录...
    # 打印【当前工作目录】（Python程序运行的目录）
    print("当前工作目录:", os.getcwd())
    # 打印【FILE_PATH的完整绝对路径】（文件实际路径）
    print("FILE_PATH 对应路径:", os.path.abspath(FILE_PATH))

if __name__ == "__main__":
    main()
pass
