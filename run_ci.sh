export CUDA_VISIBLE_DEVICES=0

# python main.py \
#         --dataset coarse-few-nerd \
#         --setting CI \
#         --model PCP \
#         --dot \
#         --only_test

python main.py \
        --dataset  fine-few-nerd \
        --setting CI \
        --model ProtoNet \
        --lr 5e-3 \
        --proto_update SDC \
        --metric dot

# python main.py \
#         --dataset stackoverflow \
#         --setting CI \ 
#         --model ProtoNet \
#         --dot \