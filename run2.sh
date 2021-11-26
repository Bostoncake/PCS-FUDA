for loss in 0.08 0.15 0.25 0.30 0.35 0.40 0.45 0.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.90 0.95 1
do
python pcs/run.py --config "config/office/W-A-1_mixmatch${loss}.json"     
done  
