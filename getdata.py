import re
import argparse
import os


print(" __  __                             _____      _   ")
print("|  \/  |                           / ____|    | |  ")
print("| \  / | ___  _ ____   _____ _ __ | |     __ _| |_ ")
print("| |\/| |/ _ \| '__\ \ / / _ \ '_ \| |    / _` | __|")
print("| |  | | (_) | |   \ V /  __/ | | | |___| (_| | |_ ")
print("|_|  |_|\___/|_|    \_/ \___|_| |_|\_____\__,_|\__|")
print("Link:https://github.com/MorvenCat/Data-extraction")


def main():
    parser = argparse.ArgumentParser(usage='%(prog)s -t 数据文件 [-o 输出文件] -p "前缀" -s "后缀"',
                                     description="这是一个用于提取数据的脚本，可根据前缀与后缀提txt、doc文档中数据。")
    parser.add_argument('-t', '--target_file', required=True, help='需要提取数据的文件')
    parser.add_argument('-o', '--output_file', default='result.txt', help='提取后数据输出的文件，默认为result.txt')
    parser.add_argument('-p', '--prefix', required=True, help='要匹配的前缀。')
    parser.add_argument('-s', '--suffix', required=True, help='要匹配的后缀。')
    args = parser.parse_args()

    if not os.path.exists(args.target_file):
        print(f"目标文件 {args.target_file} 不存在捏~(￣▽￣)~*，再检查一下吧。")
        exit()

    if not os.path.splitext(args.target_file)[1] in ['.txt', '.doc', '.docx', '.xlsx']:
        print(f"目标文件扩展名不支持。")
        exit()

    if os.path.splitext(args.target_file)[1] in ['.doc', '.docx']:
        import docx2txt
        text = docx2txt.process(args.target_file)
    elif os.path.splitext(args.target_file)[1] == '.txt':
        with open(args.target_file, "r", encoding='utf-8') as f:
            text = f.read()
    elif os.path.splitext(args.target_file)[1] == '.xlsx':
        import openpyxl
        wb = openpyxl.load_workbook(args.target_file)
        ws = wb.active
        rows = ws.values
        text = '\n'.join([''.join(map(str, row)) for row in rows])

    pattern = re.compile(re.escape(args.prefix) + r"(.*?)" + re.escape(args.suffix), re.DOTALL)

    matches = pattern.findall(text)

    with open(args.output_file, "w", encoding='utf-8') as f:
        for match in matches:
            f.write(match.strip() + "\n")

    print(f"已从 {args.target_file} 中提取数据并将其写入 {args.output_file} 中。")


if __name__ == '__main__':
    main()
