#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	return len(string) % 2 == 0

def get_num_char(string, char):
	num = 0
	for carac in string:
		if carac == char:
			num += 1
		# num += 1 if carac == 0 else 0
	return num


def get_first_part_of_name(name):
	index = name.find('-')
	newName = name[0:index]
	newName = newName[0].upper()+newName[1:]
	return 'Bonjour, '+newName


def get_random_sentence(animals, adjectives, fruits):
	return "Aujourd'hui, j'ai vu un %s s'emparer d'un panier %s plein de %s." % (random.choice(animals), random.choice(adjectives),random.choice(fruits))


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc-étienne"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
