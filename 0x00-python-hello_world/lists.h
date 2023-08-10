#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
/**
 * struct listint_s - function that describes the singly linked list
 * @n: integer
 * @next: node pointer, points to the next node.
 * Description: structure of the singly lined list for
 * the Holberton/ALX project.
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
}listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
int check_cycle(listint_t *list);
void free_listint(listint_t *head);


#endif /*LISTS_H*/
