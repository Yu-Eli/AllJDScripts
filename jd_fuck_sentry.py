with open('/etc/hosts', 'a+') as f:
    if 'sentry.io' in open('/etc/hosts').read():
        print('已屏蔽')
    else:
        f.write('\n127.0.0.1 o1098464.ingest.sentry.io\n')
        print('屏蔽成功')

print(open('/etc/hosts').read())

import os

files = os.listdir('/ql/dist')
filesraw = os.listdir('/ql/dist')
for i in filesraw:
    if os.path.isdir('/ql/dist/' + i) or '.gz' in i:
        files.remove(i)
js_sec = []
for i in files:
    with open('/ql/dist/' + i, 'r', encoding='utf-8') as f:
        if 'sentry.io' in f.read():
            print(i, '文件中含有sentry.io')
            js_sec.append(i)
for i in js_sec:
    f = open('/ql/dist/' + i, 'r', encoding='utf-8')
    file_content = f.read()
    f.close()
    f = open('/ql/dist/' + i, 'w', encoding='utf-8')
    f.write(file_content.replace('sentry.io', ''))
    f.close()
    print('屏蔽js成功', i)
