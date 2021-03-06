import torch
from torch import nn, Tensor

import logging

logger = logging.getLogger(__name__)
class NERModel(nn.Module):
    def __init__(self, my_word_encoder): 
        '''
        word_encoder: Sentence encoder
        '''
        nn.Module.__init__(self)
        self.word_encoder = nn.DataParallel(my_word_encoder)
        self.drop = nn.Dropout()

    def get_parameters_to_optimize(self):
        parameters_to_optimize = list(self.named_parameters())
        no_decay = ['bias', 'LayerNorm.bias', 'LayerNorm.weight']
        parameters_to_optimize = [
            {'params': [p for n, p in parameters_to_optimize 
                if not any(nd in n for nd in no_decay)], 'weight_decay': 0.01},
            {'params': [p for n, p in parameters_to_optimize
                if any(nd in n for nd in no_decay)], 'weight_decay': 0.0}
        ]
        return parameters_to_optimize

    def encode(self, batch) -> torch.Tensor:
        rep = self.word_encoder(batch['sentence'], batch['attention_mask'])
        rep = self.drop(rep)  # [batch_size, max_len, 768]
        rep = rep[batch['text_mask']==1]
        return rep    
    
    def forward(self, x):
        '''
        x: sentence
        return: logits, pred
        '''
        raise NotImplementedError
    
    def train_forward(self, x):
        '''
        x: sentence
        return: embedding
        '''
        raise NotImplementedError
        
    def freeze(self):
        raise NotImplementedError

    