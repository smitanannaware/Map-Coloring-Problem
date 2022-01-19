import enum
import random
import time
from collections import defaultdict
from copy import deepcopy

import plotGraph
from graph import Domain, getAustraliaGraph, getUSAGraph

backtrack_count = 0
path = []

def ifConsistent(graph, node):
    for adj in graph.adjacents[node]:
        if graph.nodes[node] == graph.nodes[adj]:
            return False
    return True


def forwardCheck(graph, node, singleton_propagation):
    color = graph.nodes[node]
    if color == Domain.NIL:
        color = graph.domains[node][0]
    for adj in graph.adjacents[node]:
        if color in graph.domains[adj] and graph.nodes[adj] == Domain.NIL:
            graph.domains[adj].remove(color)
            if singleton_propagation and len(graph.domains[adj]) == 1:
                forwardCheck(graph, adj, singleton_propagation)


def revise(graph, source, dst):
    revised = False
    source_domain = graph.domains[source]
    for src_domain_val in source_domain:
        is_consistent = False
        for dst_domain_val in graph.domains[dst]:
            if src_domain_val != dst_domain_val:
                is_consistent = True
                break
        if not is_consistent:
            source_domain.remove(src_domain_val)
            revised = True
    return revised


def minRemainingValue(graph):
    # choose fewest legal value
    # print("MRV check")
    min_vertex_dict = {}

    min_value = min([len(graph.domains[v]) for v in graph.domains if graph.nodes[v] == Domain.NIL])
    # print(min_value)
    # get fewest legal value vertex and value
    for v in graph.domains:
        if min_value == len(graph.domains[v]) and graph.nodes[v] == Domain.NIL:
            min_vertex_dict[v] = min_value

    if len(min_vertex_dict) == 1:
        # if len is 1, no tie, return vertex
        # print("from MRV got ", list(min_vertex_dict.keys())[0])
        return list(min_vertex_dict.keys())[0]
    else:
        # print("tie-breaker", min_vertex_dict)
        # tie-breaker
        return degree_heuristic(graph, min_vertex_dict)

    # check if


def degree_heuristic(graph, vertex_dict):
    # get the degree heuristic
    max_constr = float('-inf')

    for v in vertex_dict:
        if max_constr < len(graph.adjacents[v]):
            dh_vertex = v
            max_constr = len(graph.adjacents[v])
    # print("dh taking vertex ", dh_vertex)
    return dh_vertex


def leastConstrainValue(graph, vertex):
    # check all color and its adjacent vertices without that color
    # take that have fewest cancellation
    color_dict = {}
    for color in graph.domains[vertex]:
        constraint = 0
        for v in graph.adjacents[vertex]:
            if graph.nodes[v] != Domain.NIL and color in graph.domains[v]:
                constraint += 1
        color_dict[color] = constraint
    color_sorted = {k: v for k, v in sorted(color_dict.items(), key=lambda item: item[1])}.keys()
    return list(color_sorted)


def backtrack(graph, order, type, use_heuristic, print_output):
    global backtrack_count
    # print(graph.domains)
    is_consistent = True
    if order:
        if use_heuristic:
            node = minRemainingValue(graph)
            order.remove(node)
        else:
            node = order.pop()
    else:
        return True

    if not graph.domains[node]:
        order.append(node)
        backtrack_count += 1
        return False

    if use_heuristic:
        domains = leastConstrainValue(graph, node)
    else:
        domains = graph.domains[node]
    for color in domains:
        graph.nodes[node] = color

        if print_output:
            path.append((node, color.value))
            print("Try ", node, " = ", color)
        if type == 1:
            # Simple Backtracking
            if ifConsistent(graph, node):
                if backtrack(graph, order, type, use_heuristic, print_output):
                    return True
        elif type == 2 or 3:
            # Forward Checking
            domain_backup = deepcopy(graph.domains)
            if type == 3:
                forwardCheck(graph, node, True)
            else:
                forwardCheck(graph, node, False)
            # print("Domains : ", graph.domains)
            if is_consistent and backtrack(graph, order, type, use_heuristic, print_output):
                return True
            else:
                graph.domains = domain_backup
                # print("Undo Domains : ", graph.domains)
        graph.nodes[node] = Domain.NIL
        if print_output:
            path.append((node, Domain.NIL.value))
        # backtrack_count += 1
    if graph.nodes[node] == Domain.NIL:
        if print_output:
            print("Failed ", node)
        order.append(node)
        backtrack_count += 1
        return False


def backtracking_search(graph, order=[], type=1, use_heuristic=False, print_output=True):
    if backtrack(graph, order, type, use_heuristic, print_output):
        if print_output:
            print("Found Solution!!")
            print(graph.nodes)
        for key in graph.adjacents:
            for adj in graph.adjacents[key]:
                if graph.nodes[key] == graph.nodes[adj]:
                    if print_output:
                        print(key + "(" + graph.nodes[key].name + ") -> " + adj + "(" + graph.nodes[adj].name + ")")
                        print("Incorrect solution")
        return True

    else:
        if print_output:
            print("No Solution!!")
        return False


def main():
    global backtrack_count
    # Type of Algorithm
    # 1. DFS
    # 2. DFS + FC
    # 3. DFS + FC + P
    # We can change these numbers later depending on requirement

    try:
        graph_type = int(input("Please choose the map: \n"
                               "1. Australia \n2. United States of America\n"))
        min_chromatic_num = 1
        if graph_type == 1:
            for i in range(1, 5):
                graph, order = getAustraliaGraph(i)
                if backtracking_search(graph, order, 3, True, False):
                    min_chromatic_num = i
                    break
            graph, order = getAustraliaGraph(min_chromatic_num)

        elif graph_type == 2:
            for i in range(1, 5):
                graph, order = getUSAGraph(i)
                if backtracking_search(graph, order, 3, True, False):
                    min_chromatic_num = i
                    break
            graph, order = getUSAGraph(min_chromatic_num)
        else:
            raise ValueError()

        type = int(input("Please choose the method of coloring: \n"
                         "1. Depth first search only \n"
                         "2. Depth first search + forward checking\n"
                         "3. Depth first search + forward checking + propagation through singleton domains\n"))
        if type not in (1, 2, 3):
            raise ValueError()

        use_heuristic = input("Do you want to use heuristic? Yes or No: \n")
        start_time = time.time()
        backtrack_count = 0
        order_backup = deepcopy(order)  # Using it just for printing order at end in case output is lengthy
        print("Order of states: ", order)
        if use_heuristic in ('Y', 'y', 'Yes', 'yes'):
            backtracking_search(graph, order, type, True)
        else:
            backtracking_search(graph, order, type, False)
        print("Minimum Chromatic number for the selected graph is ", min_chromatic_num)
        print("No of backtrack : ", backtrack_count)
        print("Time Taken : ", time.time() - start_time)
        print("Order of states: ", order_backup)

        plotGraph.dataplot(path)
    except ValueError:
        print("Please enter correct input")


main()
