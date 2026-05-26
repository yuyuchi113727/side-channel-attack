import yaml
import torch
from model_framework import ASCADCNN
from datafactory import generate_data
from train_model import train
from test_model import test
from plot import plot_key_rank, plot_loss

if __name__ == "__main__":
    with open("config.yaml", "r", encoding="utf-8") as f: #调用超参数
        cfg = yaml.safe_load(f)

    datapath = cfg["datapath"]
    batch_size = cfg["batch_size"]
    epochs = cfg["epochs"]
    lr = cfg["lr"]
    num_attack_traces = cfg["num_attack_traces"]
    saved_pth = cfg["saved_pth"]
    loss_curve = cfg["loss_curve"]
    rank_curve = cfg["rank_curve"]
    train_select = cfg["train"]
    test_select = cfg["test"]
    
    train_loader, attack_loader, plaintext, real_key = generate_data(filepath=datapath, batch_size=batch_size)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = ASCADCNN().to(device)
    
    if train_select:
        trained_model, loss_evolution = train(model=model, epochs=epochs, lr=lr, train_loader=train_loader, device=device)
        plot_loss(loss_evolution=loss_evolution, epochs=epochs, filepath=loss_curve)
        torch.save(trained_model.state_dict(), saved_pth) #首次需要训练生成模型权重
    
    if test_select:
        model.load_state_dict(torch.load(saved_pth, map_location=device))
        rank_evolution = test(model=model, attack_loader=attack_loader, plaintext=plaintext, real_key=real_key, num_attack_traces=num_attack_traces, device=device)
        plot_key_rank(rank_evolution=rank_evolution, num_attack_traces=num_attack_traces, filepath=rank_curve)