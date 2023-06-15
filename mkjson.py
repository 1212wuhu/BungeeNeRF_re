import numpy as np
import math
import os
import json
import imageio
from sklearn.metrics import pairwise_distances

def config_parser():
    import configargparse
    parser = configargparse.ArgumentParser()
    parser.add_argument("--datadir", type=str, default='data/Norway_double', help='path to your meta')
    parser.add_argument("--latlng", type=lambda s: [float(item) for item in s.split(',')], default=[55.61328140212069,12.97634171554239], help='latlng of center building')
    parser.add_argument("--scale_split", type=lambda s: [int(item) for item in s.split(',')], default=[450,299,150,0], help='split index of each scale, mannually set for now')
    
    return parser

if __name__ == '__main__':

    parser = config_parser()
    args = parser.parse_args()
 
    with open(os.path.join(args.datadir, 't_poses_enu.json'), 'r') as f:
        data = json.load(f)
    poses1 = data['poses']
    filtered_poses1 = poses1[::5]
    data['poses'] = filtered_poses1
    data['scale_split'] = args.scale_split
    

    with open(os.path.join(args.datadir, 'poses_enu.json'), 'w') as f: 
        json.dump(data, f)

