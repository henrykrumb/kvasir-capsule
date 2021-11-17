#!/usr/bin/env python3
import os
import shutil

import click
import pandas as pd
import tqdm


@click.command()
@click.argument('split')
@click.argument('source')
@click.argument('target')
def fmain(split, source, target):
    df = pd.read_csv(split)
    
    for i, row in tqdm.tqdm(df.iterrows()):
        label = row['label']
        image = row['filename']
        target_path = os.path.join(target, label)
        os.makedirs(target_path, exist_ok=True)
        source_path = os.path.join(source, label, image)
        shutil.copyfile(source_path, os.path.join(target_path, image))


if __name__ == '__main__':
    fmain()
