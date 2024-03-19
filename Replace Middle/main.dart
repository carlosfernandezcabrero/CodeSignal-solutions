List<int> solution(List<int> arr) {
  if (arr.length.isEven == false) return arr;

  final int middle = arr.length ~/ 2;

  return arr
    ..replaceRange(middle - 1, middle + 1, [arr[middle] + arr[middle - 1]]);
}
