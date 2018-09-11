#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list)
{
	listint_t *cursor;
	listint_t *head;

	head = list;
	cursor = list;
	while (cursor != NULL && cursor->next != NULL)
	{
		head = head->next;
		cursor = cursor->next->next;
		if (head == cursor)
			return (1);
	}
	return (0);
}
