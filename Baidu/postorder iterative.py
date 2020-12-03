## Postorder Traversal Iterative Solution
def postorder(root):
	res = []
	if root == None:
		return res
	stack = []
	stack.append(root)
	while stack:
		curr = stack.pop()
		res.insert(0, curr.val)
		if curr.left != None:
			stack.append(curr.left)
		if curr.right != None:
			stack.append(curr.right)
	return res
