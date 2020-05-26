#include <stdio.h>

int main() {
	int a = 0, b = 0, c = 0;
	for (int i = 0; i < 1000; i++) {
		if (i % 3 == 0) {
			a = a + i;
		}
		if (i % 5 == 0) {
			b = b + i;
		}
		if (i % 15 == 0) {
			c = c + i;
		}
	}
	printf("%d   %d  %d\n", a, b, c);
	printf("%d", a + b - c);
	return 0;
}