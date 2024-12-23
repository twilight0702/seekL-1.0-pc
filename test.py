import deepl
import re

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

# 示例内容
content = '''
$ player_choice(
    [
      ("what the hell are you looking at", "day1_4"), 
      ("you're bluffing. i'm super secure", "day1_5")
    ]
)
'''

# 调用替换函数
new_content = replace_player_choice(content)
print(new_content)
