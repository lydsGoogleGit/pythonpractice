def findJudge(n, nodes):
    base_nodes_to_test = set([i[1] for i in nodes])  # create discrete list of 'trusted' people
    for i in nodes:
        if i[0] in base_nodes_to_test:
            base_nodes_to_test.remove(i[0])
    base_node_dict = {base_node: [] for base_node in base_nodes_to_test}
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
