#查找与替换

1.  (^13[0-9]{1,2})*(\[) 替换成 \1 __________ \2

解释: ^13表示回车;[0-9]表示0~9中的数字，{1,2}表示前面的内容重复次数，最少1次，最多2次; ()内的按顺序在替换框中对应\1,\2; \[即[([是特殊字符，要加\转义）

2.  (.)*(^13) 替换成 \1 __________ \2

