#include "lists.h"
/**
 * insert_node - insert noede tp a sorted singly list
 * @head: pointer to first node
 * @number: number to sort
 * Return: Pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp = *head, *prev;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	if (temp->n >= number)
	{
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}
	while (temp)
	{
		if (temp->n <= number)
		{
			prev = temp;
			temp = temp->next;
		}
		else
			break;
	}
	new_node->next = temp;
	prev->next = new_node;
	return (new_node);
}
