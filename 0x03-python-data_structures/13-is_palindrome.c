#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half, *prev_slow = *head;
	int result = 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	second_half = reverseList(slow);

	while (result && second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			result = 0;
		}

		*head = (*head)->next;
		second_half = second_half->next;
	}
	prev_slow->next = reverseList(slow);

	return (result);
}
/**
 * reverseList - main function
 * @head: para 1
 * Return: io
 */
listint_t *reverseList(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

