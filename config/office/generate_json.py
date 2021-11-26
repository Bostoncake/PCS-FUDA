import json

file = "/home/xiongyizhe/FUDA/PCS-FUDA/config/office/W-A-1.json"
with open(file, "r") as f:
    cont = json.load(f)

print(cont["optim_params"])
mixmatch_loss_list = [0.08, 0.15, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1]
for loss in mixmatch_loss_list:
    cont['optim_params']['mixmatch_loss'] = loss
    file = "/home/xiongyizhe/FUDA/PCS-FUDA/config/office/W-A-1" + "_mixmatch" + f"{loss}" + ".json"
    with open(file, "w") as f:
        json.dump(cont, f, ensure_ascii=False, indent=4)