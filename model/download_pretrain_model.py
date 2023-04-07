import torch
from sentence_transformers import SentenceTransformer

if __name__ == "__main__":
    pretrain_model = "paraphrase-multilingual-MiniLM-L12-v2"
    model = SentenceTransformer(pretrain_model)
    torch.save(model, "./model/sentence_embedding_model.pth")
