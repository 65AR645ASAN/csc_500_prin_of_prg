from graphviz import Digraph

# Create a new Digraph object
dot = Digraph()

# Add nodes for each step
dot.node('A', 'Start')
dot.node('B', 'Determine Number of Batches')
dot.node('C', 'Get 4 cups of flour per batch')
dot.node('D', 'Get 1/3 cup of sugar per batch')
dot.node('E', 'Get 1/5 cup of butter per batch')
dot.node('F', 'Get 1/4 Teaspoon baking powder per batch')
dot.node('G', 'Get 1 egg per batch')
dot.node('H', 'Get 2 Teaspoons of milk per batch')
dot.node('I', 'More Batches?')
dot.node('J', 'Mix Ingredients')
dot.node('K', 'Preheat Oven to 350°F')
dot.node('L', 'Shape Cookies on Baking Sheet')
dot.node('M', 'Bake for 10-12 Minutes')
dot.node('N', 'Cool Cookies')
dot.node('O', 'Serve and Enjoy')
dot.node('P', 'End')

# Add edges between the nodes
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F')
dot.edge('F', 'G')
dot.edge('G', 'H')
dot.edge('H', 'I')
dot.edge('I', 'J')
dot.edge('J', 'K')
dot.edge('K', 'L')
dot.edge('L', 'M')
dot.edge('M', 'N')
dot.edge('N', 'O')
dot.edge('O', 'P')
dot.edge('I', 'B', constraint='false')

# Render the flowchart to a file
dot.render('flowchart', format='png', view=True)
