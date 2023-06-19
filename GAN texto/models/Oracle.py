

from models.generator import LSTMGenerator


class Oracle(LSTMGenerator):

    def __init__(self, embedding_dim, hidden_dim, vocab_size, max_seq_len, padding_idx, gpu=False):
        super(Oracle, self).__init__(embedding_dim, hidden_dim, vocab_size, max_seq_len, padding_idx, gpu)
        self.name = 'oracle'

        # initialise oracle network with N(0,1)
        # otherwise variance of initialisation is very small => high NLL for loader sampled from the same model
        self.init_oracle()
