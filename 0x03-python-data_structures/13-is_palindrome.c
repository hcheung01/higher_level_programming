#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/*
 * is_palindrome - function with one argument
 * @head: pointer to linked list
 *
 * Description: check if value singly linked list is palindrome
 * Return: 1 if true or 0 if false
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int count = 0, count2 = 0, half;
	int *buf = NULL;

	if (!head)
	      return (0);
	if (!*head)
		return (1);
	ptr = *head;
	while (ptr && ptr->next)
	{
		ptr = ptr->next;
		count++;
	}
	buf = malloc(sizeof(int) * count);
	if (!buf)
		return (0);

	ptr = *head;
	count = 0;
	while (ptr)
	{
		buf[count] = ptr->n;
		count++;
		ptr = ptr->next;
	}
	half = count / 2;

	while (half)
	{
		if (buf[count2] != buf[count - 1])
			return (0);
		half--;
		count2++;
		count--;
	}
	free(buf);
	return (1);
}
