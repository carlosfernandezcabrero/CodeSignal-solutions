int solution(int candlesNumber, int makeNew) {
  int result = candlesNumber;

  while (candlesNumber >= makeNew) {
    final int newCandles = candlesNumber ~/ makeNew;

    result += newCandles;
    candlesNumber = (candlesNumber % makeNew) + newCandles;
  }

  return result;
}
