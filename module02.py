from todolist import TodoList 

FILENAME = "todos.json"

def add(todos):
    title = input("タスク名を入力 > ").strip()
    if title:
        #add関数内で.appendして要素を作っていく
        #done状態はbool変数で指定して後でmark変数に条件代入
        todos.add(title)
    else:
        print("正しくタスク名を入力してください")

def view(todos):
    if not todos.todos:
        print("タスクはありません")
        return
    #enumerateを使ってリストの要素とインデックスをとってくる
    for i, todo in enumerate(todos.todos, start=1):

        #条件付き代入文
        mark = "DONE" if todo.done else " "
        print(f"{i}: [{mark}] {todo.title}")

def select(todos):
    view(todos)
    num = input("番号を入力してください > ")
    #数字かどうかの例外処理
    if not num.isdigit():
        print("数字を入力してください")
        return None
    #numではなくてindexを返す
    index = int(num) - 1
    if 0 <= index < len(todos.todos):
        return index
    print("その番号はありません")
    return None

def complete(todos):
    #配列に関数を入れるんだったら先に変数に入れておく
    #errorとNoneは別。Noneが返ってきたときの場合を指定しておく
    index = select(todos)
    if index is not None:
        todos.complete(index)
        print("完了にしました")


def delete(todos):
    index = select(todos)
    if index is not None:
        #.pop(index)でリストから要素を消したうえで、返り値として消した要素を得ることができる
        removed = todos.delete(index)
        print(f"{removed.title}を削除しました")

def main():
    #保存したリストを読み込む
    todos = TodoList()
    todos.load(FILENAME)
    #while Trueを使うことでCUIとして継続表示
    while True:
        print("\n=== ToDoアプリ ===")
        print("1: 追加 2: 一覧 3: 完了 4: 消去　0: 終了")
        choice = input("番号を入力してください > ")

        if choice == "0":
            break
        elif choice == "1":
            add(todos)
            todos.save(FILENAME)
        elif choice == "2":
            view(todos)
        elif choice == "3":
            complete(todos)
            todos.save(FILENAME)
        elif choice == "4":
            delete(todos)
            todos.save(FILENAME)

if __name__ == "__main__":
    main()