package main

func solution(year int) int {
	twoDigitsYear := year / 100

	if lowerLimit := twoDigitsYear * 100; year > lowerLimit {
		return twoDigitsYear + 1
	}

	return twoDigitsYear
}
