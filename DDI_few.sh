for mode in train val test; do
    if [ ! -d "data/DDI/$mode" ]; then
        mkdir -p results/DDI$mode
    fi
done

export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

python3 ./main/run_prompt.py \
--data_dir ../data/DDI/k-shot/1-1 \
--output_dir ./results/DDI \
--model_type bert \
--model_name_or_path ../bert \
--per_gpu_train_batch_size 8 \
--gradient_accumulation_steps 1 \
--max_seq_length 512 \
--warmup_steps 400 \
--learning_rate 1e-4 \
--learning_rate_for_new_token 1e-5 \
--num_train_epochs 30 \
--weight_decay 1e-2 \
--adam_epsilon 1e-6 \
--temps temp.txt