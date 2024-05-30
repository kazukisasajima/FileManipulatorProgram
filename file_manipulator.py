import sys

def validate_args():
    num_args = len(sys.argv)

    if num_args < 4:
        print("引数が足りません")
        sys.exit(1)

    command = sys.argv[1]
    if command not in ['reverse', 'copy', 'duplicate-contents', 'replace-string']:
        print("無効なコマンドです")
        sys.exit(1)

    if command == 'reverse':
        if num_args != 4:
            print("Wrong reverse method usage!")
            print('Usage: python file_manipulator.py reverse inputpath outputpath')
            sys.exit(1)

    if command == 'copy':
        if num_args != 4:
            print("Wrong copy method usage!")
            print('Usage: python file_manipulator.py copy inputpath outputpath')
            sys.exit(1)

    if command == 'duplicate-contents':
        if num_args != 4 or not sys.argv[3].isdigit():
            print("Wrong duplicate-contents method usage!")
            print('Usage: python file_manipulator.py duplicate-contents inputpath n')
            sys.exit(1)

    if command == 'replace-string':
        if num_args != 5:
            print("Wrong replace-string method usage!")
            print('Usage: python file_manipulator.py replace-string inputpath needle newstring')
            sys.exit(1)


def main():
    validate_args()

    command = sys.argv[1]
    input_file_path = sys.argv[2]
	
    with open(input_file_path) as f:
        content = f.read()

    if command == 'reverse':
        output_file_path = sys.argv[3]
        new_content = ''.join(reversed(content))
        with open(output_file_path, 'w') as f:
            f.write(new_content)

    elif command == 'copy':
        output_file_path = sys.argv[3]
        new_content = content
        with open(output_file_path, 'w') as f:
            f.write(new_content)

    elif command == 'duplicate-contents':
        repeat = int(sys.argv[3])
        new_content = content + ('\n' + content) * (repeat-1)
        with open(input_file_path, 'w') as f:
            f.write(new_content)

    elif command == 'replace-string':
        search_word = sys.argv[3]
        replace_word = sys.argv[4]
        new_content = content.replace(search_word, replace_word)
        with open(input_file_path, 'w') as f:
            f.write(new_content)


if __name__ == "__main__":
    main()