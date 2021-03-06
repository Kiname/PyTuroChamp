#!/usr/bin/env python3

# A Python chess engine based on Plankalkül (1948) by Konrad Zuse

import chess as c
import sys, math, time
from random import random

# computer plays as Black by default

COMPC = c.BLACK
PLAYC = c.WHITE

MAXPLIES = 3	# maximum search depth

b = c.Board()
NODES = 0

def getval(b):
	"Get total piece value of board"
	return (
		len(b.pieces(c.PAWN, c.WHITE))          - len(b.pieces(c.PAWN, c.BLACK))
	+	2 * (len(b.pieces(c.KNIGHT, c.WHITE))   - len(b.pieces(c.KNIGHT, c.BLACK)))
	+	2 * (len(b.pieces(c.BISHOP, c.WHITE))   - len(b.pieces(c.BISHOP, c.BLACK)))
	+	3 * (len(b.pieces(c.ROOK, c.WHITE))     - len(b.pieces(c.ROOK, c.BLACK)))
	+	4 * (len(b.pieces(c.QUEEN, c.WHITE))    - len(b.pieces(c.QUEEN, c.BLACK)))
	)

# https://chessprogramming.org/Alpha-Beta
def searchmax(b, ply, alpha, beta):
	"Search moves and evaluate positions"
	global NODES

	NODES += 1
	if ply >= MAXPLIES:
		return getval(b)
	for x in order(b, ply):
		b.push(x)
		t = searchmin(b, ply + 1, alpha, beta)
		b.pop()
		if t >= beta:
			return beta
		if t > alpha:
			alpha = t
	return alpha

def searchmin(b, ply, alpha, beta):
	"Search moves and evaluate positions"
	global NODES

	NODES += 1
	if ply >= MAXPLIES:
		return getval(b)
	for x in order(b, ply):
		b.push(x)
		t = searchmax(b, ply + 1, alpha, beta)
		b.pop()
		if t <= alpha:
			return alpha
		if t < beta:
			beta = t
	return beta

def order(b, ply):
	"Move ordering"
	if ply > 0:
		return b.legal_moves
	am, bm = [], []
	for x in b.legal_moves:
		if b.is_capture(x):
			if b.piece_at(x.to_square):
				# MVV/LVA sorting (http://home.hccnet.nl/h.g.muller/mvv.html)
				am.append((x, 10 * b.piece_at(x.to_square).piece_type
							- b.piece_at(x.from_square).piece_type))
			else:	# to square is empty during en passant capture
				am.append((x, 10 - b.piece_at(x.from_square).piece_type))
		else:
			am.append((x, b.piece_at(x.from_square).piece_type))
	am.sort(key = lambda m: m[1])
	am.reverse()
	bm = [q[0] for q in am]
	return bm

def pm():
	if COMPC == c.WHITE:
		return 1
	else:
		return -1

def getmove(b, silent = False, usebook = False):
	"Get move list for board"
	global COMPC, PLAYC, MAXPLIES, NODES

	ll = []
	NODES = 0

	if b.turn == c.WHITE:
		COMPC = c.WHITE
		PLAYC = c.BLACK
	else:
		COMPC = c.BLACK
		PLAYC = c.WHITE

	if not silent:
		print(b.unicode())
		print(getval(b))
		print("FEN:", b.fen())

	nl = len(list(b.legal_moves))

	start = time.time()
	for n, x in enumerate(b.legal_moves):
		b.push(x)
		p = random()
		if COMPC == c.WHITE:
			t = searchmin(b, 0, -1e6, 1e6)
		else:
			t = searchmax(b, 0, -1e6, 1e6)
		if not silent:
			print("(%u/%u) %s %.1f %.2f" % (n + 1, nl, x, p, t))
		ll.append((x, p, t))
		b.pop()

	ll.sort(key = lambda m: m[1] + 1000 * m[2])
	if COMPC == c.WHITE:
		ll.reverse()
	print('# %.2f %s' % (ll[0][1] + ll[0][2], [str(ll[0][0])]))
	print('info depth %d score cp %d time %d nodes %d pv %s' % (MAXPLIES + 1,
		100 * pm () * ll[0][2], 1000 * (time.time() - start), NODES, str(ll[0][0])))
	return ll[0][1] + ll[0][2], [str(ll[0][0])]

if __name__ == '__main__':
	while True:	# game loop
		while True:
			print(b.unicode())
			print(getval(b))
			if sys.version < '3':
				move = raw_input("Your move? ")
			else:
				move = input("Your move? ")
			try:
				try:
					b.push_san(move)
				except ValueError:
					b.push_uci(move)
			except:
				print("Sorry? Try again. (Or type Control-C to quit.)")
			else:
				break

		if b.result() != '*':
			print("Game result:", b.result())
			break

		tt = time.time()
		t, m = getmove(b)
		print("My move: %u. %s     ( calculation time spent: %u m %u s )" % (
			b.fullmove_number, m[0],
			(time.time() - tt) // 60, (time.time() - tt) % 60))
		b.push(c.Move.from_uci(m[0]))

		if b.result() != '*':
			print("Game result:", b.result())
			break


