
for loss in 0.01 0.02 0.05 0.1 0.2
do
python pcs/run.py --config "config/office/W-A-1_mixmatch${loss}.json"     
done                             