int solution(int n) {
  int start = 1;
  int r = 0;

  for (int i = start; i < n / 2; i++) {
    int sum = 0;
    int j = i;

    while (sum < n) {
      sum += j;
      j++;
    }

    if (sum == n) r++;
  }

  return r;
}
