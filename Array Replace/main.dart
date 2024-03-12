List<int> solution(
    List<int> inputArray, int elemToReplace, int substitutionElem) {
  return inputArray
      .map((e) => e == elemToReplace ? substitutionElem : e)
      .toList();
}
