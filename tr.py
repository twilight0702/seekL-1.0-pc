import os
import deepl

# Deepl 翻译 API 密钥
api_key = "ce79d65f-6074-4fc1-bcc8-02066e67682e:fx"  # 替换为你的 Deepl API 密钥
translator = deepl.Translator(api_key)

def translate_text(text, target_language="ZH-HANS"):
    try:
        # 使用 Deepl 翻译 API 进行翻译
        target_language="ZH-HANS"
        translated_text = translator.translate_text(text, target_lang=target_language)
        return translated_text.text
    except Exception as e:
        print(f"翻译失败: {e}")
        return text


def process_rpy_file(file_path, translator):
    print(f"正在处理文件: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    for i, line in enumerate(lines):
        # 处理 'old' 行，保留原始内容，不做替换
        if line.startswith("    old "):
            new_lines.append(line)
        # 处理 'new' 行，翻译并替换其中的内容
        elif line.startswith("    new "):
            new_text = line.split('"', 1)[-1].rsplit('"', 1)[0]
            print(f"翻译中: {new_text}")
            translated_text = translate_text(new_text, translator)
            print(f"翻译结果: {translated_text}")
            new_lines.append(f'    new "{translated_text}"\n')  # 替换 new 行
        # 处理 '# o' 注释行并保持原样
        elif line.strip().startswith("# o "):
            new_lines.append(line)
        # 处理 '# voice' 注释行并保持原样
        elif line.strip().startswith("# voice "):
            new_lines.append(line)
        # 处理 'o ""' 行，翻译并替换其中的文本
        elif line.strip().startswith("o \"\""):
            original_text = line.split('"', 1)[-1].rsplit('"', 1)[0]
            print(f"翻译注释内容: {original_text}")
            translated_text = translate_text(original_text, translator)
            print(f"翻译结果: {translated_text}")
            new_line = f'    o "{translated_text}"\n'
            new_lines.append(new_line)
        # 其他行直接保留
        else:
            new_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".rpy"):
                file_path = os.path.join(root, file)
                process_rpy_file(file_path, translator)

if __name__ == "__main__":
    folder_path = "D:\\APPS\\seekl\\seekL-1.0-pc\\game\\tl\\simple_chinese\\"
    if os.path.isdir(folder_path):
        process_folder(folder_path)
        print("处理完成！")
    else:
        print("提供的路径不是一个有效的文件夹。")
