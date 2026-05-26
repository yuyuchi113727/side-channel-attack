import torch
from torch.utils.data import DataLoader, TensorDataset
import h5py
import numpy as np

def generate_data(filepath, batch_size):
    f = f = h5py.File(filepath, 'r')
    train_traces = np.array(f["Profiling_traces/traces"]) #[num, T] 功率曲线训练集
    train_labels = np.array(f["Profiling_traces/labels"]) #[num, ] Sbox(P[2]^K[2])标签训练集
    
    X_train = torch.tensor(train_traces, dtype=torch.float32)
    Y_train = torch.tensor(train_labels, dtype=torch.long)
    X_train = X_train.unsqueeze(1) #[num, 1, T]

    train_dataset = TensorDataset(X_train, Y_train)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    attack_traces = np.array(f["Attack_traces/traces"]) #[num, T] 功率曲线测试集
    metadata = f["Attack_traces/metadata"]
    plaintext = metadata["plaintext"] #明文(16字节)
    real_key = metadata["key"] #真实密钥(16字节)

    X_attack = torch.tensor(attack_traces, dtype=torch.float32)
    X_attack = X_attack.unsqueeze(1) #[num, 1, T]
    attack_loader = DataLoader(TensorDataset(X_attack), batch_size=64, shuffle=False)
    
    return train_loader, attack_loader, plaintext, real_key