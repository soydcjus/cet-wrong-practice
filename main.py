import sqlite3
import random

def init_db():
    conn = sqlite3.connect("cet6_wrong.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS wrong_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_answer TEXT,
        source TEXT
    )''')
    conn.commit()
    conn.close()

def add_question(q, a, b, c, d, ans, src):
    conn = sqlite3.connect("cet6_wrong.db")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO wrong_questions(question,option_a,option_b,option_c,option_d,correct_answer,source)
    VALUES (?,?,?,?,?,?,?)''',(q,a,b,c,d,ans,src))
    conn.commit()
    conn.close()

def get_shuffle_all():
    conn = sqlite3.connect("cet6_wrong.db")
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM wrong_questions").fetchall()
    conn.close()
    random.shuffle(rows)
    return rows

def start_practice():
    q_list = get_shuffle_all()
    if not q_list:
        print("题库为空，请先录入错题！")
        return
    total = len(q_list)
    right_cnt = 0
    for idx, item in enumerate(q_list,1):
        _id,q,opt_a,opt_b,opt_c,opt_d,correct,src = item
        print(f"\n----------第{idx}/{total}题 【来源：{src}】----------")
        print(q)
        print(f"A.{opt_a}")
        print(f"B.{opt_b}")
        print(f"C.{opt_c}")
        print(f"D.{opt_d}")
        user = input("请输入答案(A/B/C/D): ").strip().upper()
        if user == correct:
            print("✅正确")
            right_cnt +=1
        else:
            print(f"❌错误，正确答案:{correct}")
    print(f"\n练习结束，正确率：{right_cnt}/{total}  {right_cnt/total:.1%}")


if __name__ == "__main__":
    init_db()
    add_question(
        question="The _____ of the policy caused wide public concern.",
        option_a="consequence",
        option_b="advantage",
        option_c="barrier",
        option_d="phenomenon",
        correct_answer="A",
        source="2024‑06 六级仔细阅读"
    )
    add_question(
        question="Many local people hold a _____ attitude toward new technology.",
        option_a="positive",
        option_b="conservative",
        option_c="flexible",
        option_d="aggressive",
        correct_answer="B",
        source="2023‑12 六级阅读"
    )

    while True:
        print("\n=====六级错题重做系统=====")
        print("1.开始打乱重做全部错题")
        print("2.退出")
        select = input("请选择：")
        if select == "1":
            start_practice()
        elif select == "2":
            print("程序退出")
            break
        else:
            print("输入错误")
