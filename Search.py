def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    search_array = sorted_array  # 更新用変数

    # 配列の要素数が1になるまで繰り返す
    while len(search_array) > 1:
        mid = int(len(search_array) / 2)  # 配列の中間の値を参照

        # 探索対象が中間値未満の場合，中間値未満の配列を作り探索範囲を限定
        if target_number < search_array[mid]:
            search_array = search_array[:mid]

        # 探索対象が中間値以上の場合，中間値以上の配列を作り探索範囲を限定
        else:
            search_array = search_array[mid:]

    # 要素数1の配列の要素が，探索対象と等しいとき，その値を返却
    if search_array[0] == target_number:
        return sorted_array.index(search_array[0])
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
