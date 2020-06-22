root_nodes = {}

def set_assignments_by_level(roots, view_id):
    view_files = np.zeros((len(root_nodes), len(data_files)))
    for root in roots:
        for file in assignments[roots[root]]:
            view_files[root_nodes[root]][file] = assignments[roots[root]][file]
    save_np('views/all/', view_files, 'files_' + view_id)


def set_words_by_level(roots, view_id):
    view_words = np.zeros((len(root_nodes), len(words_dic)))
    for root in roots:
        for word in node_words[roots[root]]:
            view_words[root_nodes[root]][words_dic[word]] = tf_idf[root[:root.index('Z')]][word]
    save_np('views/all/', view_words, 'words_' + view_id)


def get_views_by_level():
    queues = {}
    for prefix in prefixes:
        for node in trees[prefix]:
            q_id = prefix + node['id']
            queues[q_id] = []
            queues[q_id].append(node)
    level = 0
    keep = True
    while keep:
        keep = False
        view_by_level(queues, level)
        for q in queues:
            tmp = []
            for node in queues[q]:
                for child in node['children']:
                    tmp.append(child)
            if len(tmp) > 0:
                keep = True
            queues[q] = tmp
        level += 1

def view_by_level(queues, level):
    max_q = 0
    for q in queues:
        max_q = max(max_q, len(queues[q]))
    print(max_q)
    for i in range(max_q):
        roots = {}
        for root in root_nodes:
            if i < len(queues[root]):
                roots[root] = root[:root.index('Z')] + queues[root][i]['id']
        set_assignments_by_level(roots, str(level) + '_' + str(i))
        set_words_by_level(roots, str(level) + '_' + str(i))

def decode_words_view(folder, nodes_id, view_id):
    with open(folder + "words_" + view_id + ".npy", 'rb') as f:
        view = np.load(f)
    for node in nodes_id:
        print('\n', node, nodes_id[node])
        for word in words_dic:
            if view[nodes_id[node]][words_dic[word]] != -1:
                print(word, end=', ')

def decode_files_view(folder, nodes_id, view_id):
    with open(folder + "files_" + view_id + ".npy", 'rb') as f:
        view = np.load(f)
    for node in nodes_id:
        print('\n', node, nodes_id[node])
        for file in data_files:
            if view[nodes_id[node]][file] != -1:
                print(file, end=', ')

#decode_files_view('views/nodes/', nodes, 'nodes')
#decode_words_view('views/nodes/', nodes, 'nodes')

get_views_by_level()

