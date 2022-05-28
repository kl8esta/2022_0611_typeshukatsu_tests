def main():
    # ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    i = 0               # 先頭インデックス
    j = len(array) - 1  # 末端インデックス

    # フラグ
    found_gre_equ = 0
    found_less = 0

    # ソート
    while i < j:  # 先頭と末端の検索がぶつかるまで続行

        # 先頭からの検索(基準値以上)
        if array[i] >= pivot and found_gre_equ == 0:
            new_head = array[i]  # 見つかった要素を保存
            found_gre_equ = 1
        elif found_gre_equ == 1:  # 既に見つかっていたらパス
            pass
        else:  # 基準値未満なら1つ後ろの要素へ移動
            i += 1

        # 末端からの検索(基準値未満)
        if array[j] < pivot and found_less == 0:
            new_tail = array[j]  # 見つかった要素を保存
            found_less = 1
        elif found_less == 1:  # 既に見つかっていたらパス
            pass
        else:  # 基準値以上なら1つ前の要素へ移動
            j -= 1

        # 両方向からどちらも見つかった場合，要素を入れ替え
        if found_gre_equ == 1 and found_less == 1:
            array[i] = new_tail
            array[j] = new_head
            i += 1
            j -= 1
            found_gre_equ = 0  # フラグのリセット
            found_less = 0

    # 基準値以上と基準値未満のグループに分割
    less = [x for x in array if x < pivot]
    gre_equ = [x for x in array if x >= pivot]

    # 基準値未満の要素が空となる場合，基準値以上のグループを再分割
    if less == []:
        return sort([gre_equ[0]]) + sort(gre_equ[1:])

    # 分割した各グループで同様の処理
    return sort(less) + sort(gre_equ)
    # ここまで記述

if __name__ == '__main__':
    main()
