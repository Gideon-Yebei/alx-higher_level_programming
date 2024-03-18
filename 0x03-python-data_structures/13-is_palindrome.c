#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int arr[10000];
	int i, j;

	if (*head == NULL)
		return (1);

	current = *head;
	i = 0;
	while (current != NULL)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}

	i--;
	for (j = 0; j < i; j++)
	{
		if (arr[j] != arr[i])
			return (0);
		i--;
	}

	return (1);
}
