



def is_prime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	i = 3
	while i * i <= n:
		if n % i == 0:
			return False
		i += 2
	return True


def two_digit_primes():
	return [n for n in range(10, 100) if is_prime(n)]


if __name__ == "__main__":
	primes = two_digit_primes()
	print("Two-digit prime numbers:")
	print(*primes)

