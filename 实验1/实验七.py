
# file_name122 = "scores.txt"
# math_scores = []
# english_scores = []
# student_count = 0
# try:
#     with open(file_name122, "w", encoding="utf-8") as f:
#         while True:
#             name = input("请输入学生姓名（输入'q'退出）：")
#             if name == 'q':
#                 break
#             try:
#                 math = float(input("请输入数学分数："))
#                 english = float(input("请输入英语分数："))
#                 f.write(f"{name},{math},{english}\n")
#
#                 math_scores.append(math)
#                 english_scores.append(english)
#                 student_count += 1
#             except Exception as e:
#                 print(f"出现错误：{e}")
# except Exception as e:
#     print(f"出现错误：{e}")
# try:
#     with open(file_name122, "r", encoding="utf-8") as f:
#         print("\n文件内容：")
#         for line in f:
#             print(line.strip())
#     if student_count > 0:
#         math_avg = sum(math_scores) / student_count
#         english_avg = sum(english_scores) / student_count
#         print(f"\n数学平均成绩：{math_avg:.1f}")
#         print(f"英语平均成绩：{english_avg:.1f}")
#     else:
#         print("无学生信息可统计")
# except Exception as e:
#     print(f"出现错误：{e}")

# sadSF
# def survey_statistics():
#     # 写入调查结果到文件

# data= ["不满意", "一般", "满意", "一般", "很满意", "满意",
#        "一般", "一般", "不满意", "满意", "满意", "很满意"]

# try:
#     with open(input_file, "w", encoding="utf-8") as f:
#         f.write("\n".join(data))
# except Exception as e:
#     print(f"出现错误：{e}")
input_file122 = "input.txt"
output_file122 = "stats.txt"
stats = {}
try:
    with open(input_file122, "r", encoding="utf-8") as f:
        print("调查结果内容：")
        for line in f:
            item = line.strip()
            print(item)
            if item in stats:
                stats[item] += 1
            else:
                stats[item] = 1
except Exception as e:
    print(f"：{e}")
try:
    with open(output_file122, "w", encoding="utf-8") as f:
        f.write(str(stats))
    print(f"\n统计结果已存入 {output_file122}，统计字典：{stats}")
except Exception as e:
    print(f"出现错误：{e}")
