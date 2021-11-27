import json

mixmatch_loss_list = [0.01, 0.02, 0.05, 0.08, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
mixmatch_method_list = ["source", "target", "source+target", "source-target"]
mixmatch_warmup_list = [3, 5, 7]

# file = f"/home/xiongyizhe/FUDA/PCS-FUDA/config/office/W-A-1.json"
# with open(file, "r") as f:
#     cont = json.load(f)
# for loss in mixmatch_loss_list:
#     for method in mixmatch_method_list:
#         cont["mixmatch"] = {}
#         cont["mixmatch"]["mixmatch_loss"] = loss
#         cont["mixmatch"]["mixmatch_method"] = method

#         file = f"/home/xiongyizhe/FUDA/PCS-FUDA/config/office/W-A-1_mixmatch_{method}_{loss}.json"
#         with open(file, "w") as f:
#             json.dump(cont, f, ensure_ascii=False, indent=4)


for loss in mixmatch_loss_list:
    for method in mixmatch_method_list:
        file = f"/home/xiongyizhe/FUDA/PCS-FUDA/config/office/W-A-1_mixmatch_{method}_{loss}.json"
        with open(file, "r") as f:
            cont = json.load(f)
        cont["mixmatch"]["mixmatch_enable"] = 1
        cont["mixmatch"]["mixmatch_warmup"] = 3

        
        with open(file, "w") as f:
            json.dump(cont, f, ensure_ascii=False, indent=4)