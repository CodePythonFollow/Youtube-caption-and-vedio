import os


class Deal_caption():
    def replace_srt(self, file_name):

        fi = open(file_name, 'r', encoding='utf-8')

        fo = open(f"comp-{file_name.split('/')[1]}", 'a', encoding='utf-8')
        # print(f"comp-{file_name.split('/')[1]}")

        lines = fi.readlines()

        for line in lines:
            if line == '\n':
                continue
            else:
                try:
                    int(line[0])
                    fo.write('\n' + line)
                except Exception as e:
                    fo.write(line)

        fi.close()
        fo.close()


   