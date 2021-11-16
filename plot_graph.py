import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def get_graph_plot(data, rank,file_name,title):
    plt.close()
    G = nx.DiGraph()
    node_sizes=[]
    keys = data.keys()
    flag_dict = {}
    for key in keys:
        path = f"brasao/{key}.png"
        flag = mpimg.imread(path) 
        G.add_node(key,image = flag)
        flag_dict[key] = flag
        node_sizes.append(rank[key]*9000)
        
    for key in data:
        for value in data[key]:
            G.add_edge(key,value)

    pos = nx.spring_layout(G, seed=2)

    plt.figure(figsize=(8, 6.4))
    plt.title(title)
    nx.draw(G,pos,width=1,edge_color="gray",alpha=0.8,node_color="white",node_size=node_sizes)
    ax=plt.gca()
    fig=plt.gcf()
    trans = ax.transData.transform
    trans2 = fig.transFigure.inverted().transform
    imsize = 0.05 # this is the image size
    for n in list(G.nodes()):
        (x,y) = pos[n]
        xx,yy = trans((x,y)) # figure coordinates
        xa,ya = trans2((xx,yy)) # axes coordinates
        imsize = rank[n]
        a = plt.axes([xa-imsize/2.0,ya-imsize/2.0, imsize, imsize ])
        a.imshow(flag_dict[n])
        a.set_aspect('equal')
        a.axis('off')
    plt.savefig(f'./{file_name}.png')

data = {'Avaí': ['Internacional', 'Cruzeiro', 'Botafogo-RJ', 'Vasco', 'Corinthians', 'CSA', 'Fortaleza', 'Grêmio', 'Palmeiras', 'Chapecoense', 'Ceará', 'Flamengo', 'Goiás', 'Bahia', 'São Paulo', 'Santos', 'Atlético-MG'], 'Cruzeiro': ['Avaí', 'Internacional', 'Vasco', 'CSA', 'Fluminense', 'Fortaleza', 'Grêmio', 'Palmeiras', 'Chapecoense', 'Athlético-PR', 'Flamengo', 'Goiás', 'Bahia', 'Santos', 'Atlético-MG'], 'Vasco': ['Avaí', 'Cruzeiro', 'Botafogo-RJ', 'Corinthians', 'Grêmio', 'Palmeiras', 'Athlético-PR', 'Flamengo', 'Bahia', 'São Paulo', 'Santos', 'Atlético-MG'], 'Fluminense': ['Avaí', 'Internacional', 'Botafogo-RJ', 'Vasco', 'CSA', 'Palmeiras', 'Chapecoense', 'Ceará', 'Athlético-PR', 'Flamengo', 'Goiás', 'Bahia', 'São Paulo', 'Santos', 'Atlético-MG'], 'Athlético-PR': ['Avaí', 'Botafogo-RJ', 'Corinthians', 'Fortaleza', 'Grêmio', 'Palmeiras', 'Chapecoense', 'Flamengo', 'Goiás', 'São Paulo'], 'Atlético-MG': ['Avaí', 'Internacional', 'Botafogo-RJ', 'Vasco', 'Corinthians', 'Fortaleza', 'Grêmio', 'Palmeiras', 'Chapecoense', 'Athlético-PR', 'Flamengo', 'Bahia', 'São Paulo', 'Santos'], 'Botafogo-RJ': ['Internacional', 'Cruzeiro', 'Vasco', 'Corinthians', 'Fluminense', 'Fortaleza', 'Grêmio', 'Palmeiras', 'Ceará', 'Athlético-PR', 'Flamengo', 'Goiás', 'Bahia', 'São Paulo', 'Santos', 'Atlético-MG'], 'Internacional': ['Vasco', 'Corinthians', 'CSA', 'Fluminense', 'Grêmio', 'Palmeiras', 'Chapecoense', 'Ceará', 'Athlético-PR', 'Flamengo', 'Goiás', 'São Paulo', 'Santos'], 'Corinthians': ['Internacional', 'Cruzeiro', 'Botafogo-RJ', 'CSA', 'Fluminense', 'Grêmio', 'Palmeiras', 'Flamengo', 'Bahia', 'São Paulo', 'Santos', 'Atlético-MG'], 'CSA': ['Internacional', 'Botafogo-RJ', 'Vasco', 'Corinthians', 'Fluminense', 'Fortaleza', 'Grêmio', 'Palmeiras', 'Chapecoense', 'Ceará', 'Athlético-PR', 'Flamengo', 'Goiás', 'Bahia', 'São Paulo', 'Santos', 'Atlético-MG'], 'Fortaleza': ['Internacional', 'Botafogo-RJ', 'Vasco', 'Corinthians', 'Fluminense', 'Grêmio', 'Palmeiras', 'Ceará', 'Athlético-PR', 'Flamengo', 'São Paulo', 'Atlético-MG'], 'Chapecoense': ['Internacional', 'Botafogo-RJ', 'Vasco', 'Corinthians', 'CSA', 'Fluminense', 'Fortaleza', 'Grêmio', 'Palmeiras', 'Ceará', 'Athlético-PR', 'Flamengo', 'Goiás', 'Bahia', 'São Paulo', 'Santos', 'Atlético-MG'], 'Ceará': ['Internacional', 'Cruzeiro', 'Botafogo-RJ', 'Vasco', 'Corinthians', 'CSA', 'Fortaleza', 'Grêmio', 'Palmeiras', 'Chapecoense', 'Athlético-PR', 'Flamengo', 'Goiás', 'São Paulo', 'Santos', 'Atlético-MG'], 'Flamengo': ['Internacional', 'Bahia', 'São Paulo', 'Santos', 'Atlético-MG'], 'Bahia': ['Internacional', 'Cruzeiro', 'Botafogo-RJ', 'Corinthians', 'Fluminense', 'Fortaleza', 'Palmeiras', 'Chapecoense', 'Ceará', 'Athlético-PR', 'Flamengo', 'Goiás', 'São Paulo', 'Santos'], 'São Paulo': ['Internacional', 'Cruzeiro', 'Vasco', 'Corinthians', 'Fluminense', 'Grêmio', 'Palmeiras', 'Athlético-PR', 'Flamengo', 'Goiás', 'Bahia'], 'Santos': ['Internacional', 'Cruzeiro', 'Fortaleza', 'Grêmio', 'Palmeiras', 'Athlético-PR', 'Flamengo', 'São Paulo', 'Atlético-MG'], 'Goiás': ['Cruzeiro', 'Botafogo-RJ', 'Vasco', 'Corinthians', 'CSA', 'Fortaleza', 'Grêmio', 'Palmeiras', 'Athlético-PR', 'Flamengo', 'São Paulo', 'Santos', 'Atlético-MG'], 'Grêmio': ['Corinthians', 'Fluminense', 'Fortaleza', 'Ceará', 'Athlético-PR', 'Flamengo', 'Goiás', 'Bahia', 'Santos'], 'Palmeiras': ['Corinthians', 'Fluminense', 'Grêmio', 'Ceará', 'Flamengo', 'Bahia', 'Santos']}
rank = {'Avaí': 0.023204431631854643, 'CSA': 0.02827919942992317, 'Chapecoense': 0.03267553658736824, 'Cruzeiro': 0.038001441823676284, 'Vasco': 0.03925273873191851, 'Ceará': 0.040616779161862064, 'Botafogo-RJ': 0.0413150736142469, 'Goiás': 0.044280436563128314, 'Fortaleza': 0.04502403091345658, 'Fluminense': 0.0481811999320447, 'Atlético-MG': 0.05298295432879255, 'Athlético-PR': 0.05674734170683425, 'Corinthians': 0.05889037894105191, 'Internacional': 0.05929667728343428, 'Bahia': 0.059993605387585955, 'Palmeiras': 0.06103950055701741, 'Grêmio': 0.06207870301568832, 'São Paulo': 0.06638944490059873, 'Santos': 0.06743609696100619, 'Flamengo': 0.07431442852851786}
get_graph_plot(data,rank, 'teams2019', 'Brasileiro 2019')

data = {'Coritiba': ['Fortaleza', 'Ceará', 'Flamengo', 'Santos', 'Fluminense', 'Botafogo-RJ', 'Atlético-GO', 'Corinthians', 'Goiás', 'Grêmio', 'Sport', 'São Paulo', 'Internacional', 'Athlético-PR', 'Atlético-MG', 'Bahia'], 'Fortaleza': ['Ceará', 'Flamengo', 'Bragantino', 'Fluminense', 'Atlético-GO', 'Corinthians', 'Palmeiras', 'Grêmio', 'Sport', 'São Paulo', 'Internacional', 'Athlético-PR', 'Atlético-MG', 'Bahia'], 'Bragantino': ['Fortaleza', 'Coritiba', 'Flamengo', 'Santos', 'Atlético-GO', 'Palmeiras', 'Grêmio', 'Internacional', 'Athlético-PR', 'Atlético-MG', 'Bahia'], 'Santos': ['Fortaleza', 'Flamengo', 'Bragantino', 'Fluminense', 'Atlético-GO', 'Goiás', 'Vasco', 'Palmeiras', 'Internacional', 'Athlético-PR', 'Atlético-MG', 'Bahia'], 'Botafogo-RJ': ['Fortaleza', 'Ceará', 'Flamengo', 'Bragantino', 'Santos', 'Fluminense', 'Atlético-GO', 'Corinthians', 'Goiás', 'Vasco', 'Grêmio', 'Sport', 'São Paulo', 'Internacional', 'Athlético-PR', 'Atlético-MG', 'Bahia'], 'Corinthians': ['Fortaleza', 'Ceará', 'Flamengo', 'Bragantino', 'Santos', 'Fluminense', 'Atlético-GO', 'Palmeiras', 'Grêmio', 'Sport', 'São Paulo', 'Atlético-MG', 'Bahia'], 'Goiás': ['Fortaleza', 'Ceará', 'Flamengo', 'Bragantino', 'Santos', 'Fluminense', 'Corinthians', 'Vasco', 'Grêmio', 'Sport', 'São Paulo', 'Internacional', 'Athlético-PR', 'Atlético-MG', 'Bahia'], 'Vasco': ['Fortaleza', 'Coritiba', 'Ceará', 'Flamengo', 'Bragantino', 'Fluminense', 'Atlético-GO', 'Corinthians', 'Palmeiras', 'Grêmio', 'Internacional', 'Athlético-PR', 'Atlético-MG', 'Bahia'], 'Palmeiras': ['Fortaleza', 'Coritiba', 'Ceará', 'Flamengo', 'Botafogo-RJ', 'Goiás', 'Grêmio', 'São Paulo', 'Internacional', 'Atlético-MG'], 'Grêmio': ['Fortaleza', 'Flamengo', 'Bragantino', 'Santos', 'Corinthians', 'Palmeiras', 'Sport', 'São Paulo', 'Internacional', 'Atlético-MG'], 'Sport': ['Fortaleza', 'Coritiba', 'Flamengo', 'Bragantino', 'Santos', 'Fluminense', 'Botafogo-RJ', 'Atlético-GO', 'Corinthians', 'Goiás', 'Vasco', 'Palmeiras', 'São Paulo', 'Internacional', 'Athlético-PR', 'Atlético-MG'], 'Internacional': ['Fortaleza', 'Flamengo', 'Santos', 'Fluminense', 'Corinthians', 'Goiás', 'Sport'], 'Atlético-MG': ['Fortaleza', 'Santos', 'Fluminense', 'Botafogo-RJ', 'Goiás', 'Vasco', 'Palmeiras', 'São Paulo', 'Internacional', 'Athlético-PR', 'Bahia'], 'Atlético-GO': ['Coritiba', 'Ceará', 'Bragantino', 'Corinthians', 'Goiás', 'Palmeiras', 'Grêmio', 'São Paulo', 'Internacional', 'Athlético-PR', 'Atlético-MG'], 'São Paulo': ['Coritiba', 'Ceará', 'Bragantino', 'Santos', 'Botafogo-RJ', 'Atlético-GO', 'Corinthians', 'Vasco', 'Internacional', 'Atlético-MG'], 'Flamengo': ['Ceará', 'Bragantino', 'Fluminense', 'Atlético-GO', 'São Paulo', 'Athlético-PR', 'Atlético-MG'], 'Ceará': ['Bragantino', 'Santos', 'Fluminense', 'Atlético-GO', 'Corinthians', 'Vasco', 'Palmeiras', 'Grêmio', 'Sport', 'São Paulo', 'Internacional', 'Athlético-PR', 'Atlético-MG'], 'Bahia': ['Ceará', 'Flamengo', 'Bragantino', 'Santos', 'Fluminense', 'Atlético-GO', 'Corinthians', 'Goiás', 'Palmeiras', 'Grêmio', 'Sport', 'São Paulo', 'Internacional', 'Athlético-PR'], 'Fluminense': ['Flamengo', 'Bragantino', 'Atlético-GO', 'Corinthians', 'Palmeiras', 'Grêmio', 'Sport', 'São Paulo', 'Atlético-MG'], 'Athlético-PR': ['Flamengo', 'Santos', 'Fluminense', 'Corinthians', 'Vasco', 'Palmeiras', 'Grêmio', 'Sport', 'São Paulo', 'Internacional', 'Atlético-MG', 'Bahia']}
rank = {'Botafogo-RJ': 0.026878312289746943, 'Coritiba': 0.03055030780380264, 'Vasco': 0.034652827286304186, 'Bahia': 0.03894470476601454, 'Goiás': 0.040748002765877284, 'Ceará': 0.04533196084422311, 'Sport': 0.04544559405456146, 'Grêmio': 0.04919574998997492, 'Athlético-PR': 0.05084996552663708, 'Fortaleza': 0.05096937656727836, 'Atlético-GO': 0.05330752043704014, 'Santos': 0.054513505160594014, 'Palmeiras': 0.055090913772881986, 'Corinthians': 0.055702696861611695, 'Fluminense': 0.05694879213775829, 'Bragantino': 0.05782606714661902, 'Flamengo': 0.06001227893972736, 'Internacional': 0.061290765092891414, 'São Paulo': 0.06190312809527941, 'Atlético-MG': 0.06983753046118057}
get_graph_plot(data,rank,'teams2020','Brasileiro 2020')