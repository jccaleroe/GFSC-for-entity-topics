python run_classifier_with_tfhub.py \
--data_dir=sarcasm_headlines \
--task_name=sarcasm \
--albert_hub_module_handle=https://tfhub.dev/google/albert_base/1 \
--output_dir=sarcasm_output \
--max_seq_length=128 \
--do_train=true \
--do_eval=true