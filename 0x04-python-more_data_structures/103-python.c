#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - function prints bytes information
 *
 * @p: The Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, n, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (n = 0; n < limit; n++)
		if (string[n] >= 0)
			printf(" %02x", string[n]);
		else
			printf(" %02x", 256 + string[n]);

	printf("\n");
}

/**
 * print_python_list - this function prints the list information
 *
 * @p: The Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int size, n;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (n = 0; n < size; n++)
	{
		obj = ((PyListObject *)p)->ob_item[n];
		printf("Element %ld: %s\n", n, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
