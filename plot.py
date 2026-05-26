import matplotlib.pyplot as plt

def plot_loss(loss_evolution, epochs, filepath):
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, epochs + 1), loss_evolution, color='blue', linewidth=1.5)
    
    plt.axhline(y=5.545, color='green', linestyle='--', label='Random loss (ln256)') #随机情况的熵
    plt.axhline(y=1.609, color='red', linestyle='--', label='OK loss (ln5)') #正确密钥排名前5的最大熵
    plt.title("Cross_entrophy_loss evolution", fontsize=14)
    plt.xlabel("Number of Epochs", fontsize=12)
    plt.ylabel("Loss", fontsize=12)
    
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.savefig(filepath)
    plt.close()

def plot_key_rank(rank_evolution, num_attack_traces, filepath):
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, num_attack_traces + 1), rank_evolution, color='blue', linewidth=1.5)
    
    plt.axhline(y=0, color='green', linestyle='--', label='Success (Rank 0)') #破译成功
    plt.axhline(y=4, color='red', linestyle='--', label='OK (Rank 4)') #前5时可进一步尝试候选key
    plt.title("Rank evolution (Target Byte 2)", fontsize=14)
    plt.xlabel("Number of Attack Traces", fontsize=12)
    plt.ylabel("Rank of Correct Key", fontsize=12)
    
    plt.gca().invert_yaxis() #将最好的置为最高线
    
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.savefig(filepath)
    plt.close()