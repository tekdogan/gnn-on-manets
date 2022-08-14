import torch
from torch_geometric.data import InMemoryDataset, download_url, Data


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

    def process(self):
        # Read data into huge `Data` list.
        data_list = []

        if self.pre_filter is not None:
            data_list = [data for data in data_list if self.pre_filter(data)]

        if self.pre_transform is not None:
            data_list = [self.pre_transform(data) for data in data_list]

        edge_index = getEdgeIndex()

        #data, slices = self.collate(data_list)
        data = Data(edge_index=edge_index)



        #torch.save((data, slices), self.processed_paths[0])
        torch.save(data,
                   os.path.join(self.processed.dir,'data.pt'))

    def getEdgeIndex():
        edge_feats = []
        for item in row.split(' ')
            edge_feats.append(item)


dataset = MANETDataset(root="data/")
