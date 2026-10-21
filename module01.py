def add(todos):
    title = input("タスク名を入力 > ").strip()
    if title:
        #add関数内で.appendして要素を作っていく
        #done状態はbool変数で指定して後でmark変数に条件代入
        todos.append({"title": title, "done": False})
    else:
        print("正しくタスク名を入力してください")

def view(todos):
    if not todos:
        print("タスクはありません")
        return
    #enumerateを使ってリストの要素とインデックスをとってくる
    for i, todo in enumerate(todos, start=1):

        #条件付き代入文
        mark = "DONE" if todo["done"] else " "
        print(f"{i}: [{mark}] {todo["title"]}")

def select(todos):
    view(todos)
    num = input("番号を入力してください > ")
    #数字かどうかの例外処理
    if not num.isdigit():
        print("数字を入力してください")
        return None
    #numではなくてindexを返す
    index = int(num) - 1
    if 0 <= index < len(todos):
        return index
    print("その番号はありません")
    return None

def complete(todos):
    #配列に関数を入れるんだったら先に変数に入れておく
    #errorとNoneは別。Noneが返ってきたときの場合を指定しておく
    index = select(todos)
    if index is not None:
        todos[index]["done"] = True
        print("完了にしました")


def delete(todos):
    index = select(todos)
    if index is not None:
        #.pop(index)でリストから要素を消したうえで、返り値として消した要素を得ることができる
        removed = todos.pop(index)
        print(f"{removed["title"]}を削除しました")

def main():
    #mainで空のリストを作成しておく
    todos = []
    #while Trueを使うことでCUIとして継続表示
    while True:
        print("\n=== ToDoアプリ ===")
        print("1: 追加 2: 一覧 3: 完了 4: 消去　0: 終了")
        choice = input("番号を入力してください > ")

        if choice == "0":
            break
        elif choice == "1":
            add(todos)
        elif choice == "2":
            view(todos)
        elif choice == "3":
            complete(todos)
        elif choice == "4":
            select(todos)
main()