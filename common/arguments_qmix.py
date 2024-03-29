# Time: 2019-11-05
# Author: Zachary 
# Name: QMIX
import time
import torch
import argparse

device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
#device = torch.device('cpu')
time_now = time.strftime('%y%m_%d%H%M')

def parse_args():
    parser = argparse.ArgumentParser("reinforcement learning experiments StarCraft II")

    # environment
    parser.add_argument("--map_name", type=str, default="3m", help="name of the scenario script")
    parser.add_argument("--difficulty", type=str, default='3', help="difficulty of the scenario script")
    parser.add_argument("--start_time", type=str, default=time_now, help="the time when start the game")
    parser.add_argument("--print_fre", type=int, default=10, help="the num for print log")
    parser.add_argument("--per_episode_max_len", type=int, default=120, help="maximum episode length")
    parser.add_argument("--max_episode", type=int, default=15000, help="maximum episode length")
    parser.add_argument("--num_epi4evaluation", type=int, default=10, help="the num for evaluation")
    parser.add_argument("--num_epi4enjoy", type=int, default=40, help="the num for evaluation")
    parser.add_argument("--fre_epi4evaluation", type=int, default=100, help="the num for evaluation")
    # parser.add_argument("--num-adversaries", type=int, default=1, help="number of adversaries")
    parser.add_argument("--n-agents", type=str, default=2, help="numbers of the agents")
    parser.add_argument("--opp-agents", type=str, default=1, help="numbers of the agents")
    parser.add_argument("--opp-sample-num", type=str, default=10, help="numbers of the agents")
    parser.add_argument("--num-quant", type=str, default=5, help="numbers of the quant")
    parser.add_argument("--state-dim", type=str, default=28, help="numbers of the state dim")
    parser.add_argument("--action-dim", type=str, default=5, help="numbers of the action dim")

    # core training parameters
    parser.add_argument("--device", default=device, help="torch device ")
    parser.add_argument("--tao", type=int, default=0.01, help="how depth we exchange the par of the nn")
    parser.add_argument("--lr", type=float, default=4e-5, help="learning rate for adam optimizer")
    parser.add_argument("--gamma", type=float, default=0.99, help="discount factor")
    parser.add_argument("--anneal_par", type=float, default=0.0004075, help="learning frequency")
    parser.add_argument("--reward_scale_par", type=float, default=1, help="scale the reward for small var")
    parser.add_argument("--epsilon", type=float, default=1.0, help="the init par for e-greedy")
    parser.add_argument("--max_grad_norm", type=float, default=6, help="max gradient norm for clip")
    parser.add_argument("--learning_start_episode", type=int, default=1000, help="learning start episode")
    parser.add_argument("--learning_fre", type=int, default=1, help="learning frequency")
    parser.add_argument("--tar_net_update_fre", type=int, default=200, help="epiosde for update target net")
    parser.add_argument("--memory_size", type=int, default=5000, help="number of data stored in the memory")
    parser.add_argument("--batch_size", type=int, default=32, help="number of episodes to optimize at the same time")

    parser.add_argument("--q_net_out", type=list, default=[64, 64], help="size of layers feature in q_net")
    parser.add_argument("--mix_net_out", type=list, default=[32, 1], help="size of layers feature in q_net")
    parser.add_argument("--q_net_hidden_size", type=list, default=64, help="size of hidden feature in q_net")
    parser.add_argument("--shape_hyper_b2_hidden", type=int, default=32, help="size of hidden feature in q_net")

    # checkpointing
    parser.add_argument("--fre4save_model", type=int, default=325)
    #parser.add_argument("--fre4save_model", type=int, default=400)
    #parser.add_argument("--start_save_model", type=int, default=400, help="saving the model")
    parser.add_argument("--start_save_model", type=int, default=1000, help="saving the model")
    parser.add_argument("--save_dir", type=str, default="models", help="model should be saved")
    parser.add_argument("--old_model_name", type=str, default="models/1912_162022/", help="model are loaded")

    # evaluation
    parser.add_argument("--restore", action="store_true", default=False)
    parser.add_argument("--display", action="store_true", default=False)
    parser.add_argument("--benchmark", action="store_true", default=False)
    parser.add_argument("--benchmark-iters", type=int, default=100000, help="number of iterations run for benchmarking")
    parser.add_argument("--benchmark-dir", type=str, default="./benchmark_files/", \
            help="directory where benchmark data is saved")
    parser.add_argument("--plots-dir", type=str, default="./learning_curves/", \
            help="directory where plot data is saved")
    return parser.parse_args()
