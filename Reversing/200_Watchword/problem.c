#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void flag() {
	char hex[] = {0x4d, 0x61, 0x69, 0x64, 0x61, 0x6b, 0x65, 0x43, 0x54, 0x46, 0x7b, 0x57, 0x65, 0x5f, 0x68, 0x61, 0x76, 0x65, 0x5f, 0x74, 0x6f, 0x5f, 0x64, 0x65, 0x76, 0x69, 0x73, 0x65, 0x5f, 0x76, 0x61, 0x72, 0x69, 0x6f, 0x75, 0x73, 0x5f, 0x74, 0x68, 0x69, 0x6e, 0x67, 0x73, 0x5f, 0x77, 0x68, 0x65, 0x6e, 0x5f, 0x79, 0x6f, 0x75, 0x5f, 0x63, 0x6f, 0x6e, 0x66, 0x69, 0x72, 0x6d, 0x5f, 0x74, 0x68, 0x65, 0x5f, 0x70, 0x61, 0x73, 0x73, 0x77, 0x6f, 0x72, 0x64, 0x7d};

	for (int i=0; i<sizeof(hex)/sizeof(hex[0]); i++) {
		printf("%c", hex[i]);
	}
	printf("\n");
}

int main(void) {
	char watchword[7];

	printf("Please enter watchword.\n>> ");
	scanf("%6[^\n]%*[^\n]", watchword);

	if (strcmp(watchword, "Milvas") == 0) {
		printf("Correct!!\n");
		flag();
	} else {
		printf("Watchword is incorrect.\n");
	}
}