#include "lists.h"

/**
 * check_cycle - check_cycle checks if list contains cycle
 * @list: this represents the links which is list to check
 * Return: 1 if a cycle exist, 0 if a circle does not
 */
int check_cycle(listint_t *list)
{
	listint_t *link1 = list;
	listint_t *link2 = list;

	if (!list)
		return (0);

	while (link1 && link2 && link2->next)
	{
		link1 = link1->next;
		link2 = link2->next->next;
		if (link1 == link2)
			return (1);
	}

	return (0);
}
