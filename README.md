# spack

## how to use

```bash
spack repo add /path/to/repo
spack install nuisance3 #wait a while
```

## Don't want spack to build root for you?

If you want to use an external copy of root instead of letting spack manage it, you can use the `you-can-take-my-root-but-you-can-never-take-my-freedom.py` script to put the currently-visible root environment as a non-buildable external into `~/.spack/packages.yaml`


