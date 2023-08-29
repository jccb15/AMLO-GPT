# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such

out_dir = 'out-amlo'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 250
log_interval = 5 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'amlo'
wandb_run_name = 'mini-gpt'

dataset = 'amlo'
gradient_accumulation_steps = 1
batch_size = 8
block_size = 1024 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 12
n_head = 16
n_embd = 1024
dropout = 0.2

learning_rate = 1e-4 # with baby networks can afford to go a bit higher
max_iters = 20000
lr_decay_iters = 20000 # make equal to max_iters usually
min_lr = 1e-5 # learning_rate / 10 usually
beta2 = 0.98 # make a bit bigger because number of tokens per iter is small

warmup_iters = 1000 # not super necessary potentially

# on macbook also add
# device = 'cpu'  # run on cpu only
# compile = False # do not torch compile the model
