func solution(inputString string) bool {
	result := []rune(inputString)

	for i, j := 0, len(result)-1; i < len(result)/2; i, j = i+1, j-1 {
		result[i], result[j] = result[j], result[i]
	}

	return string(result) == inputString
}
