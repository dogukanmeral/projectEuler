#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int pow(int number, int power)
{	
	int result = 1;
	for (int i=0; i<power; i++) 
	{
		result = result * number;
	};
	return result;
};

int num_length(int number, int base) 
{
	int length = 1;
	while (pow(base, length) <= number) {length++;};
	return length;
};

char int_to_ch(int i) 
{
	return i + '0';
};

char* int_to_str(int input, int base)
{	
	int length = num_length(input, base);
	char *newstr = malloc(sizeof(char[length+1]));
	newstr[length] = '\0';
	for (int i = 1; i <= length; i++)
	{
		int modusor = pow(base, i);
		int divider = pow(base, i-1);
		int digit = (input % modusor) / divider;
		newstr[length-i] = int_to_ch(digit);
	};
	return newstr;
};


int is_palindrome(char* str)
{
	if (strlen(str) <= 1) {return 1;}
	else if (str[0] != str[strlen(str)-1]) {return 0;}
	else
	{
		int new_length = strlen(str)-1;
		char smaller_str[new_length];
		smaller_str[new_length-1] = '\0';
		strncpy(&smaller_str[0], str+1, new_length-1);
		is_palindrome(smaller_str);
	};
};


int main()
{
	int sum = 0;
	for (int i = 1; i < 1000000; i++)
	{
		char* decimal = int_to_str(i, 10);
		char* binary = int_to_str(i ,2);
		if (is_palindrome(binary) && is_palindrome(decimal)) {sum += i;};
		free(decimal);
		free(binary);
	};
	printf("%d\n", sum);
	return 0;

}
