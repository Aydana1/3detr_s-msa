#!/bin/bash
#SBATCH --job-name=s_msa
#SBATCH -N1
#SBATCH -n1
#SBATCH --cpus-per-task=40
#SBATCH --mem=40G
#SBATCH --gres=gpu:1
#SBATCH --output=/l/users/aidana.nurakhmetova/thesis/S-MSA/3detr/slurms/slurm-%N-%j.out
#SBATCH --error=/l/users/aidana.nurakhmetova/thesis/S-MSA/3detr/slurms/slurm-%N-%j.err
#SBATCH --partition=gpu
#SBATCH --time=12:00:00
#SBATCH --qos=gpu-8


python main.py \
--dataset_name scannet \
--max_epoch 1080 \
--nqueries 256 \
--matcher_giou_cost 2 \
--matcher_cls_cost 1 \
--matcher_center_cost 0 \
--matcher_objectness_cost 0 \
--loss_giou_weight 1 \
--loss_no_object_weight 0.25 \
--checkpoint_dir /l/users/aidana.nurakhmetova/thesis/S-MSA/3detr/outputs/s_msa2
