import torch
import torch.nn as nn
import torch.optim as optim
import tqdm

def train(model, epochs, lr, train_loader, device):
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr=lr)
    loss_evolution = []
    
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for batch_X, batch_Y in tqdm.tqdm(train_loader, desc=f"Epoch {epoch+1}/{epochs}"):
            batch_X, batch_Y = batch_X.to(device), batch_Y.to(device)
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_Y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        avg_loss = total_loss / len(train_loader)
        print(f"Epoch {epoch+1}: loss = {avg_loss:.4f}")
        loss_evolution.append(avg_loss)
        
    return model, loss_evolution