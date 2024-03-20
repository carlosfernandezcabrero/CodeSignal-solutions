import 'dart:math';

int solution(List<int> statues) {
  final int minNumber = statues.reduce(min);
  final int maxNumber = statues.reduce(max);

  return maxNumber - minNumber - statues.length + 1;
}
