CC = python3

btree : src/main/Btree.py
	$(CC) $<

node : src/main/Node.py
	$(CC) $<

test1: src/main/test1.py
	$(CC) $<

test2: src/main/test2.py
	$(CC) $<

user: src/main/user.py
	$(CC) $<

node_test: src/main/Node_test.py
	$(CC) $<

btree_test: src/main/Btree_test.py
	$(CC) $<