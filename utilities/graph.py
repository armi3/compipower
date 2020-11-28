import graphviz
import json
import pydot
import uuid

import anytree as at
import anytree.exporter as atex
from anytree import Node, RenderTree
from anytree.dotexport import RenderTreeGraph
from anytree.exporter import DotExporter
from anytree.exporter import UniqueDotExporter

superArray = []
root = at.Node(name='root', key='root', an_attr='')
nodes = {'root': root}


def make_graph(output):
    tree_builder(output)
    # for pre, fill, node in at.RenderTree(root):
    #     print("%s%s|%s" % (pre, node.key, node.an_attr))

    atex.DotExporter(
        root, nodeattrfunc=lambda n: 'label="{}\n{}"'.format(n.key, n.an_attr)
    ).to_picture("outputs/graph.png")


def tree_builder(d, p_uid='root', l=0):
    for i, (k, v) in enumerate(d.items()):
        node_uid = uuid.uuid1()
        node = nodes[k] = at.Node(
            name=node_uid,
            key=k,
            parent=nodes[p_uid]
        )
        if isinstance(v, dict):
            node.an_attr = ''
            tree_builder(v, k, l + 1)
        else:
            node.an_attr = v

