#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function with two arguments
 * @head: head pointer to linked list
 * @number: input number
 *
 * Description: insert n value to sorted linked list
 * Return: address of new node, or NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *ahead;

	current = *head;
	ahead = current->next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL)
		*head = new;
	else if (current->next == NULL && current->n > number)
	{
		new->next = current;
		current->next = NULL;
		*head = new;
	}
	else if (current->next == NULL && current->n < number)
	{
		current->next = new;
		new->next = NULL;
	}
	else
	{
		while (ahead->next != NULL)
		{
			if (number > current->n && number < ahead->n)
			{
				current->next = new;
				new->next = ahead;
			}
			current = current->next;
			ahead = ahead->next;
		}
	}

	return (new);
}
