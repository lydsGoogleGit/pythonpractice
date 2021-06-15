def find_judge(n, nodes):
    if not nodes:
        if n == 1:
            return n
        else:
            return -1
    base_nodes_to_test = set([i[1] for i in nodes])
    for i in nodes:
        if i[0] in base_nodes_to_test:
            base_nodes_to_test.remove(i[0])
        if len(base_nodes_to_test) == 0:
            return -1
            break
    base_node_dict = {base_node: [base_node] for base_node in base_nodes_to_test}
    for key in base_node_dict:
        for truster in nodes:
            if truster[1] == key:
                base_node_dict[key].append(truster[0])
                base_node_dict[key].sort()
                print(base_node_dict)
        if list(range(1, n + 1)) == base_node_dict[key]:
            return key
        else:
            return -1
