List<int> solution(List<int> arr) {
    if (arr.isEmpty) return arr;

    int first = arr.first;
    int last = arr.last;

    arr[0] = last;
    arr[arr.length - 1] = first;

    return arr;
}
