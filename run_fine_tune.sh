export CUDA_VISIBLE_DEVICES=0

# python main.py --dataset coarse-few-nerd --protocol fine-tune --model ProtoNet --dot --use_sgd
# python main.py --dataset fine-few-nerd --protocol fine-tune --model ProtoNet --dot --use_sgd
python main.py --dataset stackoverflow --protocol fine-tune --model ProtoNet --dot --use_sgd