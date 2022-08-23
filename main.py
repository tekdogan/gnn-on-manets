import torch
from torch_geometric.data import InMemoryDataset, download_url, Data
import re
import numpy

class MANETDataset(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None, pre_filter=None):
        super().__init__(root, transform, pre_transform, pre_filter)
        #self.data, self.slices = torch.load(self.processed_paths[0])

    @property
    def raw_file_names(self):
        return 'p2p-Gnutella05.txt'

    @property
    def processed_file_names(self):
        return 'data.pt'

    def download(self):
        # Download to `self.raw_dir`.
        pass

    def getEdgeIndex(self):
        edge_indices = [[]]
        with open('data/p2p-Gnutella05.txt') as file:
            for line in file:
                #print(line)
                tmp = []
                tmp.append([int(s) for s in re.split('\t|\n|\[\,|\]',line) if s.isdigit()])
                print(tmp)
                #edge_indices.append(tmp)
                edge_indices = numpy.append(edge_indices,tmp,axis=1)
        print(len(edge_indices[0]))
        int_edge_indices = []
        for element in edge_indices:
            #print(element)
            int_edge_indices.append(int(element))
        edge_indices = torch.tensor(int_edge_indices)
        edge_indices = edge_indices.t().to(torch.long).view(2, -1)
        return edge_indices


    def process(self):
        # Read data into huge `Data` list.
        data_list = []

        if self.pre_filter is not None:
            data_list = [data for data in data_list if self.pre_filter(data)]

        if self.pre_transform is not None:
            data_list = [self.pre_transform(data) for data in data_list]

        edge_index = self.getEdgeIndex()

        #data, slices = self.collate(data_list)
        data = Data(edge_index=edge_index)



        #torch.save((data, slices), self.processed_paths[0])
        torch.save(data,
                   os.path.join(self.processed.dir,'data.pt'))


dataset = MANETDataset(root="data/")
