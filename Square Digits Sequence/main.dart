int solution(int a0) {
  final results = <int>[a0];

  while (true) {
    int auxa0 = 0;

    while (a0 > 0) {
      int digit = a0 % 10;
      a0 = a0 ~/ 10;
      auxa0 += digit * digit;
    }

    if (results.contains(auxa0)) break;

    results.add(auxa0);
    a0 = auxa0;
  }

  return results.length + 1;
}
