import torch
from sentence_transformers import SentenceTransformer

if __name__ == "__main__":
    pretrain_path = 'paraphrase-multilingual-MiniLM-L12-v2'
    model = SentenceTransformer(pretrain_path)
    torch.save(model, "./sentence_embedding_model.pth")