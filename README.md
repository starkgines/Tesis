# Tesis 

# TKC

## How to work in this project

  1. Create a enviroment with anaconda prompt 
      *conda create -n tesis
  2. Then you need to install jupyter notebook
      * with pip : pip install jupyterlab
      * with conda : conda install -c conda-forge jupyterlab
  3. add the enviroment to the kernel
      * activate tesis
      * ipython kernel install --name "tesis" --user
  4. install all dependence
    


# MobaXterm

## Computer matters
  LSB Version:    :base-4.0-amd64:base-4.0-noarch:core-4.0-amd64:core-4.0-noarch:graphics-4.0-amd64:graphics-4.0-noarch:printing-4.0-amd64:printing-4.0-noarch
  Distributor ID: CentOS
  Description:    CentOS release 6.5 (Final)
  Release:        6.5
  Codename:       Final


## User and Pass
  1. User : ssh -X -p 22000 dlconnie@200.10.231.198
  2. Pass : dlconnie@2020 
  3. source venv/bin/activate


## How to run and read with root in MobaXterm
  1. $nohup ./muonModel primary.mac > log 2> loger  
    if you want to see the progress: $ps -a **with this command line you see all the processes**
  2. $root
  3. new TBrowser()
  4. CCD1->Draw["DiffX:DiffY"] **With this command line you can see the plot of x vs y**
