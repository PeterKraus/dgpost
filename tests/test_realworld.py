import pytest
import os
import pandas as pd
import dgpost

from .utils import compare_dfs, compare_images


@pytest.mark.parametrize(
    "inpath, reflist",
    [
        (  # ts0 - load 1 dg, extract 2 keys directly
            "ts0", 
            ["peis.pkl", "data.pkl", "transform.pkl", "plot.png"],  
        ),
    ],
)
def test_realworld(inpath, reflist, datadir):
    os.chdir(datadir)
    os.chdir(inpath)
    flist = [fn for fn in sorted(os.listdir()) if fn.endswith("yaml")]
    assert len(flist) == len(reflist)
    for i, reffn in enumerate(reflist):
        dgpost.run(flist[i])
        if reffn.endswith("pkl"):
            df = pd.read_pickle(reffn)
            ref = pd.read_pickle(f"ref.{reffn}")
            compare_dfs(ref, df)
        elif reffn.endswith("png"):
            compare_images(f"ref.{reffn}", reffn)

