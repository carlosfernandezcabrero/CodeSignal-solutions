List<int> solution(List<int> inputArray, int l, int r) {
  inputArray.removeRange(l, r + 1);
  return inputArray;
}
