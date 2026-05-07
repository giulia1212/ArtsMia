from model.model import Model

mdl = Model()
mdl.buildGraph()
print(f"Il grafo creato contiene {mdl.getNumNodes()} nodi e {mdl.getNumEdges()} archi")


mdl.getInfoCompConnessa(1224)