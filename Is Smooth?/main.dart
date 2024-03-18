bool solution(List<int> arr) {
  final int isEven = arr.length % 2;
  final int middle = arr.length ~/ 2;
  final int sum = isEven == 0 ? arr[middle] + arr[middle - 1] : arr[middle];

  return arr[0] == sum && arr[arr.length - 1] == sum;
}
