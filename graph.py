import enum
import random
from copy import deepcopy


class Domain(enum.Enum):
    RED = 'lightpink'
    BLUE = 'lightskyblue'
    GREEN = 'lightgreen'
    YELLOW = 'yellow'
    ORANGE = 'orange'
    NIL = 'white'


colors = [Domain.RED, Domain.BLUE, Domain.GREEN, Domain.YELLOW, Domain.ORANGE]


class Graph:
    def __init__(self, nodes={}, adjacents={}, domains={}):
        # Dictionary nodes : Key = nodes, value = assigned color
        self.nodes = nodes
        # Dictionary adjacents : Key = node, value = adjacents of key node
        self.adjacents = adjacents
        # Dictionary domains : Key = node, value = domains of key node eg.{R, G, B}
        self.domains = domains

    def add_edge(self, u, v):
        self.nodes.setdefault(u, Domain.NIL)
        self.nodes.setdefault(v, Domain.NIL)
        self.adjacents.setdefault(u, []).append(v)
        self.adjacents.setdefault(v, []).append(u)


def create_graph(edges):
    graph = Graph()

    for edge in edges:
        src, dst = edge.split(",")
        graph.add_edge(src, dst)

    return Graph


def getUSAGraph(chromatic_num):
    #global colors
    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
              'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND',
              'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    nodes = {state: Domain.NIL for state in states}
    adjacents = {'AL': ['MS', 'TN', 'FL', 'GA'],
                 'AK': [],
                 'AZ': ['NV', 'NM', 'UT', 'CA'],  # corrected
                 'AR': ['OK', 'TN', 'TX', 'LA', 'MS', 'MO'],
                 'CA': ['OR', 'AZ', 'NV'],  # corrected
                 'CO': ['NM', 'OK', 'UT', 'WY', 'KS', 'NE'],  # AZ
                 'CT': ['NY', 'RI', 'MA'],  #
                 'DE': ['NJ', 'PA', 'MD'],
                 'FL': ['GA', 'AL'],
                 'GA': ['NC', 'SC', 'TN', 'AL', 'FL'],
                 'HI': [],
                 'ID': ['UT', 'WA', 'WY', 'MT', 'NV', 'OR'],  # corrected
                 'IL': ['KY', 'MO', 'WI', 'IN', 'IA'],  # corrected
                 'IN': ['MI', 'OH', 'IL', 'KY'],
                 'IA': ['NE', 'SD', 'WI', 'IL', 'MN', 'MO'],
                 'KS': ['NE', 'OK', 'CO', 'MO'],
                 'KY': ['TN', 'VA', 'WV', 'IL', 'IN', 'MO', 'OH'],
                 'LA': ['TX', 'AR', 'MS'],
                 'ME': ['NH'],
                 'MD': ['VA', 'WV', 'DE', 'PA'],
                 'MA': ['NY', 'RI', 'VT', 'CT', 'NH'],
                 'MI': ['OH', 'IN', 'WI'],  # corrected
                 'MN': ['ND', 'SD', 'WI', 'IA'],  # corrected
                 'MS': ['LA', 'TN', 'AL', 'AR'],
                 'MO': ['NE', 'OK', 'TN', 'AR', 'IL', 'IA', 'KS', 'KY'],
                 'MT': ['SD', 'WY', 'ID', 'ND'],
                 'NE': ['MO', 'SD', 'WY', 'CO', 'IA', 'KS'],
                 'NV': ['ID', 'OR', 'UT', 'AZ', 'CA'],
                 'NH': ['VT', 'ME', 'MA'],
                 'NJ': ['PA', 'DE', 'NY'],
                 'NM': ['OK', 'TX', 'AZ', 'CO'],  # corrected
                 'NY': ['PA', 'VT', 'CT', 'MA', 'NJ'],  # corrected
                 'NC': ['TN', 'VA', 'GA', 'SC'],
                 'ND': ['SD', 'MN', 'MT'],
                 'OH': ['MI', 'PA', 'WV', 'IN', 'KY'],
                 'OK': ['MO', 'NM', 'TX', 'AR', 'CO', 'KS'],
                 'OR': ['NV', 'WA', 'CA', 'ID'],  # corrected
                 'PA': ['NY', 'OH', 'WV', 'DE', 'MD', 'NJ'],
                 'RI': ['MA', 'CT'],  # corrected
                 'SC': ['NC', 'GA'],
                 'SD': ['NE', 'ND', 'WY', 'IA', 'MN', 'MT'],
                 'TN': ['MS', 'MO', 'NC', 'VA', 'AL', 'AR', 'GA', 'KY'],
                 'TX': ['NM', 'OK', 'AR', 'LA'],
                 'UT': ['NV', 'WY', 'AZ', 'CO', 'ID'],  # corrected
                 'VT': ['NH', 'NY', 'MA'],
                 'VA': ['NC', 'TN', 'WV', 'KY', 'MD'],
                 'WA': ['OR', 'ID'],
                 'WV': ['PA', 'VA', 'KY', 'MD', 'OH'],
                 'WI': ['MI', 'MN', 'IL', 'IA'],
                 'WY': ['NE', 'SD', 'UT', 'CO', 'ID', 'MT']}
    min_colors = colors[:chromatic_num]
    domains = {state: deepcopy(min_colors) for state in states}
    graph = Graph(nodes=nodes, adjacents=adjacents, domains=domains)
    states = ['NY', 'OH', 'NM', 'WV', 'CT', 'WA', 'ME', 'MS', 'RI', 'AZ', 'NV', 'WY', 'PA', 'TX', 'VA', 'AL', 'GA', 'NJ', 'IN', 'NH', 'SD', 'MT', 'ND', 'FL', 'SC', 'TN', 'HI', 'KY', 'OR', 'IL', 'AR', 'ID', 'MI', 'MA', 'KS', 'UT', 'IA', 'CO', 'AK', 'MD', 'LA', 'MN', 'DE', 'NE', 'NC', 'OK', 'VT', 'MO', 'CA', 'WI']

    #random.shuffle(states)
    return graph, states


def getAustraliaGraph(chromatic_num) -> Graph:
    states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    nodes = {state: Domain.NIL for state in states}

    adjacents = {'WA': ['NT', 'SA'], 'NT': ['WA', 'SA', 'Q'], 'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
                 'Q': ['NT', 'SA', 'NSW'], 'NSW': ['Q', 'SA', 'V'], 'V': ['NSW', 'SA'], 'T': []}
    min_colors = colors[:chromatic_num]
    domains = {state: deepcopy(min_colors) for state in states}
    graph = Graph(nodes=nodes, adjacents=adjacents, domains=domains)
    random.shuffle(states)
    # states = ['T', 'Q', 'SA', 'NSW', 'WA', 'V', 'NT']
    # ['Q', 'WA', 'T', 'SA', 'NSW', 'NT', 'V']
    return graph, states
