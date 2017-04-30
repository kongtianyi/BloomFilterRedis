# -*- encoding: utf-8 -*-


'''
用于检查误报的脚本
'''

def get_file_lines(path):
    '''
    文件内url数量
    '''
    lines = 0
    with open(path, 'r') as f:
        for line in f:
            lines += 1
    return lines

def get_error_count(all_path, filted_path):
    '''
    计算误报量 
    '''
    allurl = set()
    count = 0
    with open(all_path, "r") as f:
        for line in f:
            allurl.add(line)
    with open(filted_path, "r") as f:
        for line in f:
            if line not in allurl:
                count += 1
    return count

if __name__ == "__main__":
    allurl = get_file_lines("allurl.txt")
    filted = get_file_lines("filted.txt")
    print u"url总量：", allurl
    print u"过滤总量：", filted
    print u"误判总量：", get_error_count("allurl.txt", "filted.txt")