import os
import re

# 指定文件夹路径
directory_path = "D:\\APPS\\seekl\\seekL-1.0-pc\\game\\narrative"

# 遍历文件夹，找到所有.rpy文件
def get_rpy_files(directory):
    rpy_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".rpy"):
                rpy_files.append(os.path.join(root, file))
    return rpy_files

# 替换规则 1: chat_message 的处理
def replace_chat_message(content):
    pattern = r'(\$\s*chat_message\(\s*\")(.*?)(\"\))'
    replacement = r'$ chat_message(_("\2"))'
    return re.sub(pattern, replacement, content)

# 替换 player_choice 中的字符串
def replace_player_choice(content):
    # 匹配 $ player_choice([ ... ]) 的整体结构，捕获中括号内部内容
    pattern = r'(\$ player_choice\(\s*\[(.*?)\]\s*\))'

    # 替换函数
    def replacement(match):
        # 获取 player_choice 的整个内容和括号内的内容
        entire_match = match.group(1)  # 整个 $ player_choice([...]) 匹配内容
        inner_content = match.group(2)  # 中括号内部内容
        
        # 替换中括号内每一项的字符串部分
        replaced_content = re.sub(
            r'\(\s*"([^"]+)"\s*,',  # 匹配括号内第一个字符串
            r'(_("\1"),',          # 替换为添加 _("...") 的形式
            inner_content
        )

        # 将替换后的内容拼接回整个 player_choice 结构
        return f"$ player_choice([\n{replaced_content}\n])"

    # 替换整个内容中符合条件的部分
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

# 对单个文件内容进行处理
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 应用替换规则
   # content = replace_chat_message(content)
    content = replace_player_choice(content)

    # 写回修改后的内容
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# 主函数
def main():
    rpy_files = get_rpy_files(directory_path)
    for rpy_file in rpy_files:
        process_file(rpy_file)
        print(f"Processed: {rpy_file}")

if __name__ == "__main__":
    main()
